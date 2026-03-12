import pandas as pd

def load_chart_data(file_path):
    df = pd.read_csv(file_path)
    return df

def convert_df_to_text(df):
    text_data = ""
    for index, row in df.iterrows():
        text_data += ", ".join([f"{col}: {row[col]}" for col in df.columns])
        text_data += "\n"
    return text_data
