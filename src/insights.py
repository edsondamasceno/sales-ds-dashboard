def get_business_insights(df):
    produto_top = df.groupby("PRODUCTLINE")["SALES"].sum().idxmax()
    pais_top = df.groupby("COUNTRY")["SALES"].sum().idxmax()

    return produto_top, pais_top
