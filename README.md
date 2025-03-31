# TechTraders_model

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
git clone https://github.com/error-raga-008/TechTraders_model.git  
cd TechTraders_model  
```  

### 2️⃣ Install Dependencies  
```sh
pip install -r requirements.txt  
```  
Ensure you have **Python 3.8+**, **TensorFlow**, and **Flask** installed.  

### 3️⃣ Run the Stock Prediction Model on Adani Power Stock  
```sh
python "Prediction Model on Adani Power Stock/Stock_prediction_model-checkpoint.ipynb"  
```  

### 4️⃣ Run the Stock Prediction Model with Graph Feature  
```sh
python "Prediction_Model(with Graph Feature)/Stock_prediction_model.ipynb"  
```

### 5️⃣ Run the Stock Prediction Model On Datadog Inc  
```sh
python "Prediction Model on Datadog Inc/Stock_prediction_model-checkpoint.ipynb"  
```  

### 6️⃣ Configure API Key  
Before running the UI, add your Gemini API key in the `ui/test.html` file at **line 64**:  
```html
const API_KEY = "your-api-key-here";
```  

### 7️⃣ Launch Chatbot & Dashboard UI  
Simply open the UI file in your browser:  
```sh
ui/index.html  
ui/test.html  
```

### 🌐 Live Demo  
- [AI-Powered Financial Model Assistant Chatbot](https://ai-stockmarket-financial-assistant.netlify.app/)  
- [AI-Powered Financial Chatbot With Gemini](https://ai-powred-financial-chatbot-gdg.netlify.app/)  

---

## 📊 Model Performance  

✅ **Achieved Accuracy:** 65% (R² Score: 0.65)  
✅ **Tested on:** 2015-2024 stock data  
✅ **Predicted stock prices for:** June 2024  

*This model is trained on **Adani Power stocks** and predicts **June 2024 stock prices** based on **news sentiment and historical data from 2010 to May 2024**.  

Additionally, we tested this model on **Datadog Inc**, which successfully predicted the **January 2024 stock price** with high accuracy.  

---

## 🎯 Future Enhancements  

🚀 **Deploy as a Full-Fledged Chatbot** with Financial Assistant Features  
🚀 **Integrate with Google Cloud Vertex AI** for Scalable Predictions  
🚀 **Enhance Accuracy** with Reinforcement Learning  

---

## 🚀 Current Integration Status  

✅ **Stock Prediction Model**: Fully functional and can be executed using the provided:  
- `Prediction_Model(with Graph Feature)/Stock_prediction_model.ipynb`  
- `Prediction Model on Adani Power Stock/Stock_prediction_model-checkpoint.ipynb`  
- `Prediction Model on Datadog Inc/Stock_prediction_model-checkpoint.ipynb`  

✅ **Chatbot & UI**: The `test.html` and `index.html` files are working properly and can be accessed through a browser.  

---

## 🤝 Contributors  

👥 **Team Members**  
- **Vishvesh Sharma**  
- **Rishi Rami**  
- **Krish Savaliya**  

---

## 📢 Submission Links  

🔗 **Google Drive MVP Link:** [Click here](https://drive.google.com/drive/u/0/folders/1mEkpHnyDVfx_SHxb94X3iIvl6zxyJV8Z)  
🎥 **Demo Video:** [Watch here](https://youtu.be/KqnEQ0DMg9c?si=yCju-WLICqk8K107)  

---

## 🛠️ Contributing  

We welcome contributions to enhance **TechTraders_model**. To contribute:  

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

We extend our gratitude to the **open-source community** and **resources** that have contributed to the development of **TechTraders_model**.  
```

