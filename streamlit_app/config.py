from pathlib import Path

# source local
DATA_SOURCE_TYPE = "local"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SUPERSTORE_PATH = DATA_DIR / "superstore.arrow"

# source GitHub
#DATA_SOURCE_TYPE = "git"
#SUPERSTORE_PATH = "https://raw.githubusercontent.com/texodus/superstore-arrow/master/superstore.arrow"

APP_TITLE = "Superstore Sales Dashboard"

TABS = {
    "main": ["Dashboard", "Data Explorer"],
    "dashboard": [
        "Sales & Profit",
        "Discount vs Profit",
        "Top Products",
    ],
}

UI_TEXT = {
    "pagination_info": "Showing rows {start}–{end} of {total}",
    "search_label": "Search across all columns",
    "filters_header": "Filters",
    "year": "Year",
    "region": "Region",
    "category": "Category",
    "key_metrics": "Key Metrics",
    "total_sales": "Total Sales",
    "total_profit": "Total Profit",
    "total_orders": "Total Orders",
    "sales_over_time": "Sales Over Time",
    "discount_impact_title": "Discount Impact on Profit",
    "quick_insight_title": "Quick Insight",
    "sales_vs_profit_title": "Sales vs Profit",
    "top_10_products_title": "Top 10 Products by Sales",
    "sales_by_category_title": "Sales by Category",
}

COLUMNS = {
    "year": "Year",
    "region": "Region",
    "category": "Category",
    "sales": "Sales",
    "profit": "Profit",
    "orders": "Order ID",
}

BUTTON_LABELS = {
    "previous": "⬅️ Previous",
    "next": "Next ➡️",
}

ROWS_PER_PAGE = 50