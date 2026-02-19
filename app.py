import streamlit as st
import plotly.express as px

from src.data_loader import load_data
from src.kpi import compute_kpis
from src.rfm import calculate_rfm
from src.forecast import sales_forecast
from src.insights import get_business_insights

st.set_page_config(page_title="Sales DS Dashboard", layout="wide")

st.title("📊 Sales Data Science Dashboard")

# ======================
# CARREGAR DADOS
# ======================
df = load_data()

# ======================
# KPIs
# ======================
st.header("📈 KPIs")

receita, quantidade, clientes = compute_kpis(df)

col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"${receita:,.2f}")
col2.metric("Quantidade Vendida", int(quantidade))
col3.metric("Clientes", clientes)

# ======================
# VENDAS POR PAÍS
# ======================
st.header("🌎 Vendas por País")

vendas_pais = df.groupby("COUNTRY")["SALES"].sum().reset_index()
fig = px.bar(vendas_pais, x="COUNTRY", y="SALES")
st.plotly_chart(fig, use_container_width=True)

# ======================
# RFM
# ======================
st.header("👥 Segmentação de Clientes")

rfm = calculate_rfm(df)
st.dataframe(rfm.sort_values("Monetary", ascending=False).head(10))

# ======================
# FORECAST
# ======================
st.header("🔮 Previsão de Vendas")

model, forecast = sales_forecast(df)
fig_forecast = model.plot(forecast)
st.pyplot(fig_forecast)

# ======================
# INSIGHTS AUTOMÁTICOS
# ======================
st.header("🤖 Insights")

produto_top, pais_top = get_business_insights(df)

st.write(f"Produto mais vendido: **{produto_top}**")
st.write(f"Mercado mais forte: **{pais_top}**")
