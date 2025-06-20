import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def publisher_article_counts(df):
    return df['publisher'].value_counts()

def plot_headline_length_dist(df):
    plt.figure(figsize=(8, 4))
    sns.histplot(df['headline_length'], bins=30, kde=True)
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_articles_over_time(df):
    df['date_only'] = df['date'].dt.date
    daily_counts = df.groupby('date_only').size()
    daily_counts.plot(figsize=(10, 4), title="Articles Published Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.tight_layout()
    plt.show()
