import pandera as pa
from pandera import Column

schema = pa.DataFrameSchema({
    "Order ID": Column(pa.String, coerce=True),
    "Ship Mode": Column(pa.String, coerce=True),
    "Customer ID": Column(pa.String, coerce=True),
    "Customer Name": Column(pa.String, coerce=True),
    "Segment": Column(pa.String, coerce=True),
    "Country": Column(pa.String, coerce=True),
    "City": Column(pa.String, coerce=True),
    "State": Column(pa.String, coerce=True),
    "Postal Code": Column(pa.String, coerce=True),
    "Region": Column(pa.String, coerce=True),
    "Product ID": Column(pa.String, coerce=True),
    "Category": Column(pa.String, coerce=True),
    "Sub-Category": Column(pa.String, coerce=True),
    "Product Name": Column(pa.String, coerce=True),
})