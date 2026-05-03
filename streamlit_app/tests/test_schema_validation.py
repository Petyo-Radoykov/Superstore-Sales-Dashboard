from streamlit_app.domain.schema import schema

def test_schema_validation(superstore_df):
    # if schema is imported
    validated_df = schema.validate(superstore_df)

    assert validated_df.equals(superstore_df)