from streamlit_app.config import COLUMNS

def test_filters_reduce_data(superstore_df):
    # pick a single known value
    sample_year = superstore_df[COLUMNS["year"]].iloc[0]
    sample_region = superstore_df[COLUMNS["region"]].iloc[0]
    sample_category = superstore_df[COLUMNS["category"]].iloc[0]

    filtered = superstore_df[
        (superstore_df[COLUMNS["year"]] == sample_year) &
        (superstore_df[COLUMNS["region"]] == sample_region) &
        (superstore_df[COLUMNS["category"]] == sample_category)
    ]

    # filtered data should be smaller or equal
    assert len(filtered) <= len(superstore_df)

    # filtered data should only contain selected values
    assert filtered[COLUMNS["year"]].nunique() == 1
    assert filtered[COLUMNS["region"]].nunique() == 1
    assert filtered[COLUMNS["category"]].nunique() == 1