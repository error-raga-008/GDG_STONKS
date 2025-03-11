import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from transformers import pipeline
import torch

import joblib  # Only for consistency if you still need it for imputer, etc.
import pickle  # If you prefer pickle for loading/saving Python objects beyond Keras
import datetime

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

try:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
except ImportError:
    raise ImportError("Please install PyTorch by running 'pip install torch'")

# 1) Load data
stock_data = pd.read_csv('stock_data.csv')
news_data = pd.read_csv('news_data.csv')

if 'news_summary' not in news_data.columns:
    raise KeyError("The 'news_summary' column is not found in news_data.csv.")
if 'date' not in news_data.columns:
    raise KeyError("The 'date' column is not found in news_data.csv.")
if 'date' not in stock_data.columns:
    raise KeyError("The 'date' column is not found in stock_data.csv.")

# 2) Initialize sentiment pipeline
sentiment_pipeline = pipeline(
    'sentiment-analysis',
    model='distilbert-base-uncased-finetuned-sst-2-english',
    device=0 if torch.cuda.is_available() else -1
)

# 3) Preprocess news_data
news_data['sentiment'] = news_data['news_summary'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
news_data['sentiment'] = news_data['sentiment'].map({'POSITIVE': 1, 'NEGATIVE': -1, 'NEUTRAL': 0})
news_data['date'] = pd.to_datetime(news_data['date'], format='%d/%m/%Y')
news_data = news_data.groupby('date').agg({'sentiment': 'mean'}).reset_index()

# Fill missing dates daily for news
news_data = news_data.set_index('date').resample('D').ffill().reset_index()

# 4) Preprocess stock_data
stock_data['date'] = pd.to_datetime(stock_data['date'], format='%d/%m/%Y %H:%M:%S')
stock_data = stock_data.set_index('date').resample('D').ffill().reset_index()

# 5) Merge data
merged_data = pd.merge(stock_data, news_data, on='date', how='left')
print("Merged data before filtering:")
print(merged_data)

# 6) Prepare features and targets
X = merged_data[['sentiment', 'volume']]  # shape = (num_samples, 2)
y_close = merged_data['close']
y_open = merged_data['open']

imputer_X = SimpleImputer(strategy='mean')
imputer_y_close = SimpleImputer(strategy='mean')
imputer_y_open = SimpleImputer(strategy='mean')

X = imputer_X.fit_transform(X)  # shape = (num_samples, 2)
y_close = imputer_y_close.fit_transform(y_close.values.reshape(-1, 1)).ravel()
y_open = imputer_y_open.fit_transform(y_open.values.reshape(-1, 1)).ravel()

# For a simple LSTM, we treat each day as a single timestep.
# Reshape X to [samples, time_steps=1, features].
X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

# 7) Split data
X_train, X_test, y_train_close, y_test_close = train_test_split(X, y_close, test_size=0.2, shuffle=False)
_, _, y_train_open, y_test_open = train_test_split(X, y_open, test_size=0.2, shuffle=False)

# 8) Build LSTM models
def build_lstm_model():
    model = Sequential()
    model.add(LSTM(64, input_shape=(1, 2), return_sequences=False))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

model_close = build_lstm_model()
model_open = build_lstm_model()

# 9) Train the LSTM models (you can adjust epochs/batch_size)
model_close.fit(X_train, y_train_close, epochs=10, batch_size=16, verbose=1)
model_open.fit(X_train, y_train_open, epochs=10, batch_size=16, verbose=1)

# 10) Evaluate the models
y_pred_close = model_close.predict(X_test)
y_pred_open = model_open.predict(X_test)

mse_close = mean_squared_error(y_test_close, y_pred_close)
mse_open = mean_squared_error(y_test_open, y_pred_open)
print(f"LSTM MSE (Close): {mse_close}")
print(f"LSTM MSE (Open): {mse_open}")

# 11) Save the models
model_close.save('stock_price_model_close.h5')
model_open.save('stock_price_model_open.h5')

##############################################################
# Prediction function using the LSTM models
##############################################################
def predict_stock_price(news_data_file, output_file):
    # Load new news data
    new_data = pd.read_csv(news_data_file)
    
    if 'news_summary' not in new_data.columns:
        raise KeyError("The 'news_summary' column is not found in the news_data_file.")
    if 'date' not in new_data.columns:
        raise KeyError("The 'date' column is not found in the news_data_file.")
    
    new_data['sentiment'] = new_data['news_summary'].apply(lambda x: sentiment_pipeline(x)[0]['label'])
    new_data['sentiment'] = new_data['sentiment'].map({'POSITIVE': 1, 'NEGATIVE': -1, 'NEUTRAL': 0})
    new_data['date'] = pd.to_datetime(new_data['date'], format='%d/%m/%Y')
    new_data['volume'] = 0
    
    X_new = new_data[['sentiment', 'volume']]
    X_new = imputer_X.transform(X_new)  # same imputer from training
    # reshape for LSTM: (samples, 1, features=2)
    X_new = np.reshape(X_new, (X_new.shape[0], 1, X_new.shape[1]))
    
    # Load the trained LSTM models
    lstm_close = tf.keras.models.load_model('stock_price_model_close.h5')
    lstm_open = tf.keras.models.load_model('stock_price_model_open.h5')
    
    predictions_close = lstm_close.predict(X_new).ravel()
    predictions_open = lstm_open.predict(X_new).ravel()
    
    new_data['predicted_close'] = predictions_close
    new_data['predicted_open'] = predictions_open
    new_data['predicted_avg'] = (new_data['predicted_open'] + new_data['predicted_close']) / 2
    
    # Group by date to get daily averages
    daily_data = new_data.groupby('date', as_index=False).agg({
        'predicted_open': 'mean',
        'predicted_close': 'mean',
        'predicted_avg': 'mean'
    })
    
    # Create a daily date range
    min_date, max_date = daily_data['date'].min(), daily_data['date'].max()
    all_dates = pd.date_range(start=min_date, end=max_date, freq='D')
    
    # Reindex to ensure a row for every day in the range
    daily_data = (daily_data
                  .set_index('date')
                  .reindex(all_dates)
                  .rename_axis('date')
                  .reset_index())
    
    # Forward-fill any missing predictions
    daily_data[['predicted_open', 'predicted_close', 'predicted_avg']] = (
        daily_data[['predicted_open', 'predicted_close', 'predicted_avg']].ffill()
    )
    
    # Save CSV
    daily_data.to_csv(output_file, index=False)
    return daily_data

predictions = predict_stock_price('new_news_data.csv', 'predicted_stock_prices.csv')
print(predictions)