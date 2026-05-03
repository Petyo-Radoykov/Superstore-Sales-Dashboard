from pathlib import Path
import pytest
from streamlit_app.data.loader import load_data

@pytest.fixture(scope="session")
def superstore_df():
    DATA_SOURCE_TYPE = "local"
    BASE_DIR = Path(__file__).resolve().parents[1]
    DATA_DIR = BASE_DIR / "data"
    SUPERSTORE_PATH = DATA_DIR / "superstore.arrow"

    return load_data(DATA_SOURCE_TYPE, SUPERSTORE_PATH)