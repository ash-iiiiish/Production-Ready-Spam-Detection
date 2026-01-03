import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df.columns = ["label", "message"]
    return df
