# GDG_STONKS  

## Overview  

TechTraders Model is an AI-powered stock market prediction system that uses deep learning (LSTM) and sentiment analysis to forecast stock prices accurately. The model achieves **65% accuracy** and is designed to be integrated into a financial assistant chatbot in the future.  

---

## 🚀 Features  

### 🔹 AI-Powered Stock Prediction  
- Predicts **opening and closing stock prices** using **LSTM models**.  
- Analyzes **historical stock data (2015-2024)** for trend forecasting.  
- Calculates **technical indicators** (Moving Averages, Volatility, Daily Change).  

### 🔹 Sentiment Analysis on Financial News  
- Uses **DistilBERT (Hugging Face Transformers)** for sentiment scoring.  
- Analyzes news headlines to determine market sentiment.  
- Integrates with stock data to **enhance prediction accuracy**.  

### 🔹 Interactive AI Chatbot  
- **Conversational AI** to answer financial queries.  
- Integrated with **Google Gemini-Flash 2.0 API** for dynamic responses.  
- Supports **text, images, and graph-based responses**.  

### 🔹 Data Visualization  
- **Chart.js** for rendering **real-time stock graphs**.  
- Uses **Matplotlib** for actual vs. predicted stock price comparison.  

### 🔹 Data Storage & Database Support  
- **Stores stock and news data in MySQL** for structured analysis.  
- **Supports CSV exports** for external data handling.  

### 🔹 Real-Time News Scraper  
- **Collects real-time news articles** related to specific stocks.  
- Uses **Selenium & BeautifulSoup** for automated web scraping.  
- Integrates sentiment analysis for a **comprehensive stock evaluation**.  

---

## 🛠️ Technologies Used  

### **📌 Machine Learning & Deep Learning**  
- **TensorFlow & Keras** – LSTM-based stock price prediction.  
- **Scikit-learn** – Data preprocessing, scaling, and evaluation metrics.  
- **Hugging Face Transformers** – Sentiment analysis on financial news.  

### **📌 Web Development**  
- **HTML, Tailwind CSS** – UI design for chatbot and response selection.  
- **JavaScript (Chart.js)** – Graph visualization.  

### **📌 Backend & APIs**  
- **Python (Flask, Pandas, NumPy)** – Data processing and API handling.  
- **Google Gemini AI API** – AI-generated financial insights.  

### **📌 Web Scraping**  
- **Selenium & BeautifulSoup** – Extracting real-time financial news.  

### **📌 Database & Data Storage**  
- **MySQL** – Storing stock and news data for model training.  
- **CSV** – Data storage for stock predictions and scraped news.  

---

## ⚙️ Installation  

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

### 3️⃣ Run the Stock Prediction Model  
```sh
python Prediction_Model/Stock_prediction_model.ipynb  
```  

### 4️⃣ Launch Chatbot & Dashboard UI  
Simply open the UI file in your browser:  
```sh
ui/test.html  
```  

---

## 📁 File Structure  

```
Tech_Traders/
│── 📁 Prediction_Model/  
│   │── stock_price_model_close.h5         # LSTM model for closing price prediction  
│   │── stock_price_model_open.h5          # LSTM model for opening price prediction  
│   │── stock_data.csv                      # Historical stock price dataset  
│   │── news_data.csv                       # Financial news dataset  
│   │── predicted_stock_prices.csv          # AI-generated stock predictions  
│   │── Stock_prediction_model.ipynb        # Jupyter Notebook for stock prediction model  
│  
│── 📁 assets/                             # Folder for storing images  
│   │── Accuracy.jpg                       # Model accuracy visualization  
│   │── ChatBot_result.jpg                  # Chatbot prediction output  
│   │── Chatbot_Ui.jpg                      # User interface of the chatbot  
│   │── DataBase_tables.jpg                 # Database schema and tables  
│   │── flowchart.png                       # System flowchart diagram  
│   │── logo.jpg                            # Project or company logo  
│   │── Model_Error_Analysis.jpg            # Model error evaluation analysis  
│   │── Model_sample_code_Snippet.png       # Sample code snippet from the model  
│  
│── 📁 ui/                                 # Folder for UI-related files  
│   │── test.html                           # HTML file for UI  
│  
│── 📁 database/                           # Folder for database-related files  
│   │── database.sql                        # SQL file for database setup  
│  
│── 📜 LICENSE                             # Open-source license file  
│── 📜 .gitignore                          # Ignore unnecessary files  
│── 📜 README.md                           # Documentation & setup instructions  
│── 📜 requirements.txt                     # List of required Python dependencies  
```

---

## 📊 Model Performance  

✅ **Achieved Accuracy:** 65% (R² Score: 0.65)  
✅ **Tested on:** 2015-2024 stock data  
✅ **Predicted stock prices for:** June 2024  

---

## 🎯 Future Enhancements  

🚀 **Deploy as a Full-Fledged Chatbot** with Financial Assistant Features  
🚀 **Integrate with Google Cloud Vertex AI** for Scalable Predictions  
🚀 **Enhance Accuracy** with Reinforcement Learning  

---

## 🚀 Current Integration Status  

✅ **Stock Prediction Model**: Fully functional and can be executed using the provided `Stock_prediction_model.ipynb`.  
✅ **Chatbot & UI**: The `test.html` file is working properly and can be accessed through a browser.  

🚧 **Ongoing Development:**  
- **Database Integration:** While the `database.sql` file has been created, it is **not yet connected** to the chatbot or prediction model.  
- **Chatbot AI:** We are planning to enhance the chatbot with **real-time stock insights, user authentication, and live news updates**.  
- **Improved Automation:** The future version will **automatically fetch stock and news data** instead of relying on manually updated CSV files.  

### **🛠️ Future Roadmap**  
🔹 **Integrate MySQL database** for structured storage and real-time queries.  
🔹 **Improve chatbot functionalities** to provide AI-driven stock market insights.  
🔹 **Enhance prediction accuracy** with Reinforcement Learning and live data feeds.  

---

## 🤝 Contributors  

👥 **Team Members**  
- **Vishvesh Sharma**  
- **Rishi Rami**  
- **Krish Savaliya**  

---

## 📢 MVP Submission Link  

🔗 **Google Drive MVP Link:** [Insert Your MVP Link Here]  

---

## 🛠️ Contributing  

We welcome contributions to enhance **GDG_STONKS**. To contribute:  

1. **Fork the repository.**  
2. **Create a new branch:**  
   ```sh
   git checkout -b feature-name
   ```
3. **Make your changes and commit them:**  
   ```sh
   git commit -m "Add new feature"
   ```
4. **Push to the branch:**  
   ```sh
   git push origin feature-name
   ```
5. **Submit a pull request.**  

---

## 📜 License  

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.  

---

## 🙌 Acknowledgements  

We extend our gratitude to the **open-source community** and **resources** that have contributed to the development of **GDG_STONKS**.  
```

