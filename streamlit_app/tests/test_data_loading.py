from streamlit_app.data.loader import load_data
from pathlib import Path
import requests

def test_git_url_is_raw():
    
    url = "https://raw.githubusercontent.com/texodus/superstore-arrow/master/superstore.arrow"
    r = requests.get(url)

    assert r.status_code == 200
    assert "html" not in r.headers.get("Content-Type", "").lower()


def test_load_data_from_git():

    DATA_SOURCE_TYPE = "git"
    SUPERSTORE_PATH = "https://raw.githubusercontent.com/texodus/superstore-arrow/master/superstore.arrow"

    df = load_data(
        DATA_SOURCE_TYPE,
        SUPERSTORE_PATH
    )

    assert df is not None
    assert len(df) > 0
    assert "Row ID" in df.columns
    assert "Order ID" in df.columns
    assert "Order Date" in df.columns
    assert "Ship Date" in df.columns
    assert "Ship Mode" in df.columns
    assert "Customer ID" in df.columns
    assert "Customer Name" in df.columns
    assert "Segment" in df.columns
    assert "Country" in df.columns
    assert "City" in df.columns
    assert "State" in df.columns
    assert "Postal Code" in df.columns
    assert "Region" in df.columns
    assert "Product ID" in df.columns
    assert "Category" in df.columns
    assert "Sub-Category" in df.columns
    assert "Product Name" in df.columns
    assert "Sales" in df.columns
    assert "Quantity" in df.columns
    assert "Discount" in df.columns
    assert "Profit" in df.columns


def test_load_data_from_local():

    DATA_SOURCE_TYPE = "local"
    BASE_DIR = Path(__file__).resolve().parents[1]
    DATA_DIR = BASE_DIR / "data"
    SUPERSTORE_PATH = DATA_DIR / "superstore.arrow"

    df = load_data(
        DATA_SOURCE_TYPE,
        SUPERSTORE_PATH
    )

    assert df is not None
    assert len(df) > 0
    assert "Row ID" in df.columns
    assert "Order ID" in df.columns
    assert "Order Date" in df.columns
    assert "Ship Date" in df.columns
    assert "Ship Mode" in df.columns
    assert "Customer ID" in df.columns
    assert "Customer Name" in df.columns
    assert "Segment" in df.columns
    assert "Country" in df.columns
    assert "City" in df.columns
    assert "State" in df.columns
    assert "Postal Code" in df.columns
    assert "Region" in df.columns
    assert "Product ID" in df.columns
    assert "Category" in df.columns
    assert "Sub-Category" in df.columns
    assert "Product Name" in df.columns
    assert "Sales" in df.columns
    assert "Quantity" in df.columns
    assert "Discount" in df.columns
    assert "Profit" in df.columns   


def test_sales_column_valid():

    DATA_SOURCE_TYPE = "local"
    BASE_DIR = Path(__file__).resolve().parents[1]
    DATA_DIR = BASE_DIR / "data"
    SUPERSTORE_PATH = DATA_DIR / "superstore.arrow"

    df = load_data(
        DATA_SOURCE_TYPE,
        SUPERSTORE_PATH
    )

    assert df is not None
    assert len(df) > 0
    assert df["Sales"].min() >= 0
    assert df["Profit"].notnull().all()
