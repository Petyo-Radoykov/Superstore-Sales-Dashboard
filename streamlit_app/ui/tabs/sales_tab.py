import streamlit as st
import plotly.express as px
from streamlit_app.config import UI_TEXT

def render_sales_tab(filtered_df):

    st.markdown(f"### {UI_TEXT['sales_vs_profit_title']}")

    col1, col2 = st.columns(2)

    # ---------- Sales by Category ----------
    with col1:
        sales_category = (
            filtered_df.groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            sales_category,
            x="Category",
            y="Sales"
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="tab_sales_category"
        )

    # ---------- Profit by Region ----------
    with col2:
        profit_region = (
            filtered_df.groupby("Region")["Profit"]
            .sum()
            .reset_index()
        )

        fig2 = px.bar(
            profit_region,
            x="Region",
            y="Profit"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True,
            key="tab_profit_region"
        )