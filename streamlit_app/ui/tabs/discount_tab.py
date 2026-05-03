import streamlit as st
import plotly.express as px
from streamlit_app.config import UI_TEXT

def render_discount_tab(filtered_df):

    st.markdown(f"### {UI_TEXT['discount_impact_title']}")

    # Scatter plot: Discount vs Profit
    fig = px.scatter(
        filtered_df,
        x="Discount",
        y="Profit",
        opacity=0.6
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="tab_discount_profit_scatter"
    )

    # Quick insight section
    st.markdown(f"### {UI_TEXT['quick_insight_title']}")

    avg_profit_by_discount = (
        filtered_df.groupby("Discount")["Profit"]
        .mean()
        .reset_index()
    )

    fig2 = px.line(
        avg_profit_by_discount,
        x="Discount",
        y="Profit"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="tab_discount_profit_trend"
    )