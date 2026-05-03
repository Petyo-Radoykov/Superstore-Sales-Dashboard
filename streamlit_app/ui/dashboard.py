import streamlit as st
import plotly.express as px
from streamlit_app.ui.tabs.sales_tab import render_sales_tab
from streamlit_app.ui.tabs.discount_tab import render_discount_tab
from streamlit_app.ui.tabs.products_tab import render_products_tab
from streamlit_app.config import TABS, UI_TEXT, COLUMNS

def render_dashboard(filtered_df, df):

    st.subheader(UI_TEXT['key_metrics'])

    col1, col2, col3 = st.columns(3)

    col1.metric(
        UI_TEXT['total_sales'],
        f"${filtered_df[COLUMNS["sales"]].sum():,.0f}",
        f"{filtered_df[COLUMNS["sales"]].sum() - df[COLUMNS["sales"]].sum():,.0f}"
    )

    col2.metric(
        UI_TEXT['total_profit'],
        f"${filtered_df[COLUMNS["profit"]].sum():,.0f}",
        f"{filtered_df[COLUMNS["profit"]].sum() - df[COLUMNS["profit"]].sum():,.0f}"
    )

    col3.metric(
        UI_TEXT['total_orders'],
        filtered_df[COLUMNS["orders"]].nunique(),
        filtered_df[COLUMNS["orders"]].nunique() - df[COLUMNS["orders"]].nunique()
    )

    st.subheader(UI_TEXT['sales_over_time'])

    sales_time = filtered_df.groupby("Order Date")[COLUMNS["sales"]].sum().reset_index()
    fig_main = px.line(sales_time, x="Order Date", y="Sales")
    st.plotly_chart(fig_main, use_container_width=True)


    tabs = st.tabs(TABS["dashboard"])

    with tabs[0]:
        render_sales_tab(filtered_df)

    with tabs[1]:
        render_discount_tab(filtered_df)

    with tabs[2]:
        render_products_tab(filtered_df)