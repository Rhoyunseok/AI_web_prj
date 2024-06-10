import pandas as pd
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def load_csv_files(file_paths):
    dataframes = []
    for file_path in file_paths:
        encoding = detect_encoding(file_path)
        df = pd.read_csv(file_path, encoding=encoding)
        dataframes.append(df)
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df


def search_by_name(df, name):
    results = df[df['name'].str.lower() == name.lower()]
    return results
