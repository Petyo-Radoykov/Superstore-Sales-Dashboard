import streamlit as st
from streamlit_app.config import UI_TEXT, COLUMNS

def render_sidebar(df):
    st.sidebar.header(UI_TEXT['filters_header'])

    year = st.sidebar.multiselect(
        UI_TEXT["year"],
        sorted(df[COLUMNS["year"]].unique()),
        default=sorted(df[COLUMNS["year"]].unique())
    )

    region = st.sidebar.multiselect(
        UI_TEXT["region"],
        df[COLUMNS["region"]].unique(),
        default=df[COLUMNS["region"]].unique()
    )

    category = st.sidebar.multiselect(
        UI_TEXT["category"],
        df[COLUMNS["category"]].unique(),
        default=df[COLUMNS["category"]].unique()
    )

    return year, region, category