import pandas as pd

def load_data(path="/data/sales_data_sample.csv"):
    df = pd.read_csv(path, encoding="latin-1")
    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
    return df
