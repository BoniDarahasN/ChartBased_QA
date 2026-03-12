import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

def clean_data(df):
    df = df.dropna()
    return df

