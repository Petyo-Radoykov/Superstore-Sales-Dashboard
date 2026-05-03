import streamlit as st
from streamlit_app.config import APP_TITLE, DATA_SOURCE_TYPE, SUPERSTORE_PATH, TABS
from streamlit_app.data.loader import load_data
from streamlit_app.services.filtering import apply_filters
from streamlit_app.utils.logging import setup_logging
from streamlit_app.ui.sidebar import render_sidebar
from streamlit_app.ui.dashboard import render_dashboard
from streamlit_app.ui.explorer import render_explorer


setup_logging()

st.title(APP_TITLE)

df = load_data(
    source_type=DATA_SOURCE_TYPE,
    path=SUPERSTORE_PATH
)

year, region, category = render_sidebar(df)

filtered_df = apply_filters(df, year, region, category)

main_tabs = st.tabs(TABS["main"])

with main_tabs[0]:
    render_dashboard(filtered_df, df)

with main_tabs[1]:
    render_explorer(filtered_df)