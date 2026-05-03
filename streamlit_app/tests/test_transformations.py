import pandas as pd
from streamlit_app.domain.transformations import transform
from streamlit_app.config import COLUMNS

def test_transform_does_not_change_row_count(superstore_df):
    transformed = transform(superstore_df)

    assert len(transformed) == len(superstore_df)


def test_transform_keeps_required_columns(superstore_df):
    transformed = transform(superstore_df)

    required_cols = [
        COLUMNS["sales"],
        COLUMNS["profit"],
        COLUMNS["orders"]
    ]

    for col in required_cols:
        assert col in transformed.columns


def test_transform_does_not_introduce_null_sales(superstore_df):
    transformed = transform(superstore_df)

    assert transformed[COLUMNS["sales"]].notnull().all()

def test_profit_column_is_numeric(superstore_df):
    transformed = transform(superstore_df)

    assert pd.api.types.is_numeric_dtype(transformed["Profit"])    