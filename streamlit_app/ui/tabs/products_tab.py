import streamlit as st
import plotly.express as px
from streamlit_app.config import UI_TEXT

def render_products_tab(filtered_df):

    st.markdown(f"### {UI_TEXT['top_10_products_title']}")

    top_products = (
        filtered_df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Product Name",
        y="Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="tab_top_products_bar"
    )

    # Category breakdown
    st.markdown(f"### {UI_TEXT['sales_by_category_title']}")

    category_sales = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        category_sales,
        names="Category",
        values="Sales"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="tab_category_sales_pie"
    )