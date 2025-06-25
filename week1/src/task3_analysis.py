import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

from data_loader import load_news_data
from task2_analysis import load_stock_data_from_csv


def get_sentiment(text):
    """Compute sentiment polarity for a headline (-1 to +1)."""
    return TextBlob(str(text)).sentiment.polarity


def compute_daily_sentiment(news_df):
    """Convert timestamps to dates and compute average sentiment per day."""
    news_df['date'] = pd.to_datetime(news_df['date']).dt.date
    news_df['sentiment'] = news_df['headline'].apply(get_sentiment)
    daily_sentiment = news_df.groupby('date')['sentiment'].mean().reset_index()
    daily_sentiment.rename(columns={'sentiment': 'avg_daily_sentiment'}, inplace=True)
    return daily_sentiment


def compute_stock_returns(stock_df):
    """Compute daily return percentage for stock."""
    stock_df = stock_df.copy()
    stock_df['date'] = stock_df.index.date
    stock_df['daily_return'] = stock_df['close'].pct_change()
    return stock_df.reset_index(drop=True)


def merge_sentiment_and_returns(stock_df, sentiment_df):
    """Merge the two datasets on the 'date' column."""
    merged = pd.merge(stock_df, sentiment_df, on='date', how='inner')
    return merged


def correlation_analysis(merged_df):
    """Compute and print Pearson correlation, show scatter plot."""
    corr_matrix = merged_df[['daily_return', 'avg_daily_sentiment']].corr()
    print("\n📈 Correlation Matrix:\n", corr_matrix)

    sns.scatterplot(data=merged_df, x='avg_daily_sentiment', y='daily_return')
    plt.title("Sentiment vs Daily Stock Return")
    plt.xlabel("Average Daily Sentiment")
    plt.ylabel("Stock Daily Return")
    plt.grid(True)
    plt.show()