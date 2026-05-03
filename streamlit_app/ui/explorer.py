import streamlit as st
import plotly.express as px
from streamlit_app.config import UI_TEXT, BUTTON_LABELS, ROWS_PER_PAGE

def render_explorer(filtered_df):
    rows_per_page = ROWS_PER_PAGE

    # ---------- SEARCH ----------
    search_term = st.text_input(UI_TEXT['search_label'])

    if search_term:
        display_df = filtered_df[
            filtered_df.apply(
                lambda col: col.astype(str).str.contains(search_term, case=False)
            ).any(axis=1)
        ]
        st.session_state.page = 1
    else:
        display_df = filtered_df

    # ---------- CHART ----------
    st.markdown(f"### {UI_TEXT['sales_over_time']}")

    sales_time = display_df.groupby("Order Date")["Sales"].sum().reset_index()
    fig = px.line(sales_time, x="Order Date", y="Sales")
    st.plotly_chart(
        fig,
        use_container_width=True,
        key="explorer_sales_time_chart"
    )

    # ---------- PAGINATION ----------
    total_rows = len(display_df)
    total_pages = max((total_rows - 1) // rows_per_page + 1, 1)

    if "page" not in st.session_state:
        st.session_state.page = 1

    if st.session_state.page > total_pages:
        st.session_state.page = 1

    page = st.session_state.page

    start_idx = (page - 1) * rows_per_page
    end_idx = start_idx + rows_per_page

    paginated_df = display_df.iloc[start_idx:end_idx]

    # ---------- TABLE ----------
    st.dataframe(paginated_df, use_container_width=True)

    # ---------- CONTROLS ----------
    col_left, col_right = st.columns([3, 2])



    with col_left:
        st.caption(
            UI_TEXT["pagination_info"].format(
                start=start_idx + 1,
                end=min(end_idx, total_rows),
                total=total_rows,
            )
        )

    with col_right:
        btn1, btn2 = st.columns(2)

        with btn1:
            if st.button(BUTTON_LABELS["previous"]) and page > 1:
                st.session_state.page -= 1

        with btn2:
            if st.button(BUTTON_LABELS["next"]) and page < total_pages:
                st.session_state.page += 1