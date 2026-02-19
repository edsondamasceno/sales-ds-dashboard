import datetime as dt

def calculate_rfm(df):
    snapshot_date = df["ORDERDATE"].max() + dt.timedelta(days=1)

    rfm = df.groupby("CUSTOMERNAME").agg({
        "ORDERDATE": lambda x: (snapshot_date - x.max()).days,
        "ORDERNUMBER": "count",
        "SALES": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]
    return rfm
