# 📊 News & Stock Market Correlation Analysis

A data analysis project that explores the relationship between financial news headlines and stock price movements using sentiment analysis and technical indicators.

---

## 📌 Overview

This project investigates whether there's a correlation between the tone of financial news and the daily movement of stock prices. The analysis involves:

- Extracting and visualizing patterns in financial news articles.
- Applying technical indicators to stock price data.
- Conducting sentiment analysis on news headlines.
- Measuring the correlation between news sentiment and stock returns.

---

## 🛠 What I Built

### ✔ Task 1: News Data EDA
- Loaded and cleaned raw news data from CSV.
- Visualized:
  - Article distribution by time
  - Headline length
  - Top publishers and keywords
- Extracted insights from publisher domains and headline content.

### ✔ Task 2: Stock Data Analysis
- Loaded AAPL historical stock price data.
- Calculated:
  - 20-day Simple Moving Average (SMA)
  - 14-day Relative Strength Index (RSI)
  - MACD & Signal Line
- Visualized trends using `matplotlib`.

### ✔ Task 3: Sentiment & Correlation
- Applied sentiment analysis on news headlines using `TextBlob`.
- Computed average daily sentiment scores.
- Calculated daily returns of stock prices.
- Measured correlation (Pearson) between sentiment and stock movement.

---

## 💻 Tech Stack

| Tool/Library       | Purpose                                 |
|--------------------|------------------------------------------|
| `pandas`           | Data manipulation & analysis             |
| `matplotlib`       | Data visualization                       |
| `seaborn`          | Statistical visualization (EDA)          |
| `TextBlob`         | Sentiment analysis                       |
| `finta`            | Financial technical indicators           |
| `scipy.stats`      | Correlation analysis                     |
| `datetime`, `re`   | Date parsing and regex operations        |

---

## 📂 Project Structure

```bash
week1/
├── data/
│   ├── raw_analyst_ratings.csv
│   └── yfinance_data/
│       └── AAPL_historical_data.csv
├── src/
│   ├── data_loader.py           # Loads news data
│   ├── eda.py                   # Exploratory data analysis
│   ├── task2_analysis.py        # Stock indicators
│   ├── task3_analysis.py        # Sentiment & correlation
├── README.md                    # You're reading this :)
└── documentation.txt            # Full development log
```

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/Ola-je/Tenx-projects/tree/main/week1
cd Tenx-projects/week1
```

### 2. Install Dependencies
Make sure you’re using **Python 3.10+**. Then run:
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:
```bash
pip install pandas matplotlib seaborn textblob finta scipy
```

### 3. Run the Analysis
Navigate to the `src/` folder and run:
```bash
python task3_analysis.py
```

---

## 📈 Output

The program prints and plots:
- News article statistics and patterns
- Stock price trends with indicators
- Daily sentiment vs. stock return correlation

---

## 🧠 What I Learned

- Real-world data cleaning and handling missing columns
- Calculating and visualizing technical stock indicators
- Applying NLP to financial news
- Merging time-aligned datasets and analyzing correlations
- Debugging module and file path issues in Python projects

---

## 🔮 Future Work

- Improve sentiment analysis using transformers or FinBERT
- Add support for multiple stocks and publishers
- Build an interactive dashboard (e.g., with Streamlit or Dash)
- Expand analysis window (weekly/monthly trends)
- Train a model to predict stock movement from news headlines

---

## 🙌 Acknowledgments

Thanks to the mentors and reviewers at Tenx Academy guiding the Week 1 challenge. This project helped me explore the intersection of NLP, financial markets, and data science in practice.

---

**Author:** Eyerusalem Gebrekirstos  
**Contact:** kidanejerry523@gmail.com | LinkedIn: https://www.linkedin.com/in/eyerusalem-gebrekirstos
