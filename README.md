
# GDG_STONKS

## Overview

TechTraders Model is an AI-powered stock market prediction system that uses deep learning (LSTM) and sentiment analysis to forecast stock prices accurately. The model achieves 65% accuracy and is designed to be integrated into a financial assistant chatbot in the future.

## Features

- **News Scraper**: Collects real-time news articles related to specific stocks.  
- **Sentiment Analysis**: Evaluates the sentiment of news articles to determine their potential impact on stock prices.  
- **Data Integration**: Combines news sentiment data with historical stock prices for comprehensive analysis.  
- **Predictive Modeling**: Utilizes machine learning algorithms to forecast future stock price movements based on integrated data.  
- **Stock Price Prediction**: Uses LSTM to predict future stock prices based on historical trends.  
- **News Sentiment Analysis**: Incorporates real-time financial news impact on stock predictions.  
- **Interactive Chatbot UI**: A Gemini AI-powered chatbot to assist users with investment queries.  
- **Live Market Data Integration**: Fetches stock data using Yahoo Finance & Google Finance APIs.  
- **Database Support**: Stores stock data and user interactions in MySQL.  

*Note: These features currently function independently but will be integrated into a unified system in the future.*  

## Technologies Used  

- **Machine Learning & AI**: TensorFlow, Keras (LSTM-based stock prediction).  
- **Natural Language Processing (NLP)**: Google Gemini API (Sentiment analysis for market insights).  
- **Backend API**: Flask / FastAPI (Model Deployment).  
- **Frontend**: HTML, Tailwind CSS, JavaScript (Stock dashboard & chatbot UI).  
- **Database**: MySQL (Stores historical stock data & user inputs).  


## Installation
  
### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/TechTraders_model.git  
cd TechTraders_model  
```  

### 2️⃣ Install Dependencies  
```sh
pip install -r requirements.txt  
```  
Ensure you have **Python 3.8+**, **TensorFlow**, and **Flask** installed.  

### 3️⃣ Set Up MySQL Database  
```sh
mysql -u root -p  
CREATE DATABASE stock_prediction;  
USE stock_prediction;  
SOURCE database_backup.sql;  
```  

### 4️⃣ Run the Stock Prediction Model  
```sh
python Stock_prediction_model.ipynb  
```  

### 5️⃣ Launch Chatbot & Dashboard UI  
```sh
# Open test.html in your browser
```  
```

## Usage

1. **Run the News Scraper**:

   ```bash
   python news_scraper.py
   ```

2. **Perform Sentiment Analysis**:

   ```bash
   python sentiment_analysis.py
   ```

3. **Train the Predictive Model**:

   ```bash
   python train_model.py
   ```

4. **Make Predictions**:

   ```bash
   python predict.py
   ```

## File Structure
Tech_Traders/

📁 Prediction_Model/
│── stock_price_model_close.h5        # LSTM model for closing price prediction  
│── stock_price_model_open.h5         # LSTM model for opening price prediction  
│── stock_data.csv                     # Historical stock price dataset  
│── news_data.csv                      # Financial news dataset  
│── predicted_stock_prices.csv         # AI-generated stock predictions  
│── Stock_prediction_model.ipynb       # Jupyter Notebook for stock prediction model  
│  
│── 📁 assets/                          # Folder for storing images  
│   ├── Accuracy.jpg                    # Model accuracy visualization  
│   ├── ChatBot_result.jpg               # Chatbot prediction output  
│   ├── Chatbot_Ui.jpg                   # User interface of the chatbot  
│   ├── DataBase_tables.jpg              # Database schema and tables  
│   ├── flowchart.png                    # System flowchart diagram  
│   ├── logo.jpg                         # Project or company logo  
│   ├── Model_Error_Analysis.jpg         # Model error evaluation analysis  
│   ├── Model_sample_code_Snippet.png    # Sample code snippet from the model  
│  
│── 📁 ui/                              # Folder for UI-related files  
│   ├── test.html                       # HTML file for UI  
│  
│── 📁 database/                        # Folder for database-related files  
│   ├── database.sql                     # SQL file for database setup 
│ 
│── 📁 news_scraper/                    # Folder for detailed news scraping scripts and data  
│   ├── 📁 adani/                         # Subfolder for Adani-related news  
│   │   ├── data.csv                      # Raw stock data  
│   │   ├── Stocks.csv                    # Processed stock dataset  
│   │   ├── news.csv                      # Financial news dataset  
│   ├── adani_power_news_fixed.csv        # Fixed news dataset for Adani Power  
│   ├── chromedriver.exe                  # Web driver for scraping  
│   ├── news.py                           # Python script for fetching news  
│   ├── test.py                           # Test script for news scraping  
│  
│── 📁 extra/                           # Folder for additional datasets and backups  
│   ├── new_news_data.csv                 # Additional news dataset  
│   ├── news_data.csv                     # Backup of the main news dataset  
│   ├── old_predicted_stock_prices.csv     # Previous predicted stock prices  
│   ├── stock_data.csv                     # Backup of the main stock dataset  
│   ├── xx_news_data.csv                   # Extra financial news dataset  
│   ├── xx_stock_data.csv                  # Extra stock dataset  
│  
│── 📜 LICENSE                              # Open-source license file  
│── 📜 .gitignore                           # Ignore unnecessary files  
│── 📜 README.md                            # Documentation & setup instructions  
│── 📜 requirements.txt                      # List of required Python dependencies  

## Contributing

We welcome contributions to enhance GDG_STONKS. To contribute:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m 'Add new feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature-name
   ```

5. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

We extend our gratitude to the open-source community and resources that have contributed to the development of GDG_STONKS.

