from streamlit_app.config import COLUMNS

#golden dataset test
def test_dataset_shape_stability(superstore_df):
    assert superstore_df.shape[0] >= 9994
    assert superstore_df.shape[1] >= 22

def test_dataset_columns_exist(superstore_df):
    for col in COLUMNS.values():
        assert col in superstore_df.columns    