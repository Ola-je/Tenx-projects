from numpy import vectorize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


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

def extract_topics(headlines, num_topics = 5, num_words = 5):
    vectorizer = CountVectorizer(stop_words='english', max_df=0.95, min_df=2)
    X = vectorizer.fit_transform(headlines)
    
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(X)

    words = vectorizer.get_feature_names_out()
    topics = []

    for idx, topic in enumerate(lda.components_):
        top_words = [words[i] for i in topic.argsort()[:-num_words - 1:-1]]
        topics.append((f"Topic {idx+1}", top_words))

    return topics

def plot_articles_per_hour(df):
    df['publish_hour'] = df['date'].dt.hour
    hourly_counts = df['publish_hour'].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(x=hourly_counts.index, y=hourly_counts.values, color='skyblue')
    plt.title("Articles Published by Hour of Day")
    plt.xlabel("Hour (0–23)")
    plt.ylabel("Number of Articles")
    plt.xticks(range(0, 24))
    plt.tight_layout()
    plt.show()

def plot_articles_per_day(df):
    df['publish_day'] = df['date'].dt.date
    daily_counts = df.groupby('publish_day').size()

    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    plt.title("Articles Published Per Day")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def top_publishers(df, top_n=10):
    return df['publisher'].value_counts().head(top_n)

def publisher_keywords(df, top_n=5):
    top_pubs = df['publisher'].value_counts().head(top_n).index

    for pub in top_pubs:
        pub_headlines = df[df['publisher'] == pub]['headline']
        vectorizer = CountVectorizer(stop_words='english', max_features=10)
        word_matrix = vectorizer.fit_transform(pub_headlines)
        top_words = vectorizer.get_feature_names_out()
        print(f"\nTop words for {pub}: {', '.join(top_words)}")

def extract_email_domains(df):
    df_email = df[df['publisher'].str.contains('@', na=False)].copy()
    df_email['domain'] = df_email['publisher'].apply(lambda x: x.split('@')[-1])
    return df_email['domain'].value_counts()
