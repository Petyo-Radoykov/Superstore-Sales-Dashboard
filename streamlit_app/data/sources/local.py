import pandas as pd
import pyarrow as pa
import pyarrow.ipc as ipc

from .base import DataSource

class LocalArrowSource(DataSource):
    def __init__(self, path: str):
        self.path = path

    def load(self) -> pd.DataFrame:
        with open(self.path, "rb") as f:
            reader = ipc.open_stream(pa.BufferReader(f.read()))
            table = reader.read_all()
        return table.to_pandas()