import streamlit as st
from streamlit_app.domain.schema import schema
from streamlit_app.domain.transformations import transform
from streamlit_app.utils.exceptions import DataLoadError
from streamlit_app.data.sources.local import LocalArrowSource
from streamlit_app.data.sources.git import GitArrowSource

@st.cache_data
def load_data(source_type: str, path: str):
    try:
        if source_type == "local":
            source = LocalArrowSource(path)

        elif source_type == "git":
            source = GitArrowSource(path)

        else:
            raise ValueError(f"Unsupported source_type: {source_type}")
        
        df = source.load()

        df = transform(df)
        df = schema.validate(df)

        return df

    except Exception as e:
        raise DataLoadError(str(e)) from e