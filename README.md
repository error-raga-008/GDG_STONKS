
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

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/error-raga-008/GDG_STONKS.git
   cd GDG_STONKS
   ```

2. **Install Dependencies**:

   Ensure you have Python installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:

   Create a `.env` file in the root directory and add necessary configuration variables, such as API keys for news sources.

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

- `news_scraper.py`: Script for scraping news articles.
- `sentiment_analysis.py`: Performs sentiment analysis on news data.
- `train_model.py`: Trains the predictive model using integrated data.
- `predict.py`: Generates stock price predictions.
- `requirements.txt`: Lists all Python dependencies.
- `data/`: Directory containing datasets like `news_data.csv` and `stock_data.csv`.

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

