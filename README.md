# Superstore-Sales-Dashboard
# Superstore Sales Dashboard

A **Streamlit-based interactive dashboard** for exploring and analyzing Superstore sales data using the `superstore.arrow` dataset. This project demonstrates clean architecture, data validation, and rich visualizations for business insights.

---

## 🚀 Features

* Interactive sales and profit dashboards
* Data exploration with filtering and search
* Visualizations powered by Plotly
* Data validation using Pandera schemas
* Fast data loading with PyArrow
* Test coverage with Pytest

---

## 📁 Project Structure

```text
Python_charts/
│
├── app.py                     # Entry point for Streamlit app
├── pyproject.toml             # Project configuration (Poetry)
└── streamlit_app/
    ├── config.py              # Configuration and constants
    ├── data/                  # Data loading and sources
    ├── domain/                # Schema and transformations
    ├── services/              # Business logic (filters, etc.)
    ├── utils/                 # Utilities (logging, exceptions)
    └── ui/                    # UI components (dashboard, sidebar, explorer)
```

---

## 📦 Requirements

* Python >= 3.12
* Dependency management via **Poetry** (defined in `pyproject.toml`)

---

## ⚙️ Installation (Poetry)

This project uses **Poetry** instead of `requirements.txt`.

### 1. Install Poetry (if not installed)

```bash
pip install poetry
```

---

### 2. Install dependencies

From the project root:

```bash
poetry install
```

---

### 3. Activate the virtual environment

```bash
poetry shell
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

---

## 🧪 Running Tests

```bash
pytest
```

Or via Poetry:

```bash
poetry run pytest
```

---

## 📊 Data Source

The dashboard uses the **Superstore dataset** stored in Apache Arrow format:

```text
streamlit_app/data/superstore.arrow
```

You can switch between local and remote (GitHub) data sources in:

```text
streamlit_app/config.py
```

Example:

```python
DATA_SOURCE_TYPE = "local"  # or "git"
```

---

## 🧱 Architecture Highlights

* **Modular design** separating UI, data, domain logic, and services
* **Schema validation** using Pandera to ensure data integrity
* **Pluggable data sources** (local or remote)
* **Reusable UI components**

---

## 📦 Dependencies (managed via pyproject.toml)

* streamlit
* pandas
* pandera
* plotly
* pyarrow
* requests
* pytest

---

## 👤 Author

**Petyo Emilov Radoykov**
📧 [petyoradoykov@gmail.com](mailto:petyoradoykov@gmail.com)

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

## 💡 Future Improvements

* Deploy to Streamlit Cloud / Docker
* Add advanced analytics (forecasting, clustering)
* Improve performance for large datasets
* Add user authentication

---

## ⭐ Acknowledgements

* Superstore dataset (public domain)
* Streamlit for rapid UI development
* Plotly for visualization

---

