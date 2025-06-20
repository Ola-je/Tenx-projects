import pandas as pd

def load_news_data(file_path):
    df = pd.read_csv(file_path)
    
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date'] = df['date'].dt.tz_localize(None)
    df['headline_length'] = df['headline'].astype(str).apply(len)
    
    return df