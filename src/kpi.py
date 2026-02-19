def compute_kpis(df):
    receita = df["SALES"].sum()
    quantidade = df["QUANTITYORDERED"].sum()
    clientes = df["CUSTOMERNAME"].nunique()
    return receita, quantidade, clientes
