from prophet import Prophet

def sales_forecast(df, periods=90):
    df_prophet = df.groupby("ORDERDATE")["SALES"].sum().reset_index()
    df_prophet.columns = ["ds", "y"]

    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return model, forecast
