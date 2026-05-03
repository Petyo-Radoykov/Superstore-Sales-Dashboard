import pandas as pd
import requests
import pyarrow as pa
import pyarrow.ipc as ipc

from .base import DataSource

class GitArrowSource(DataSource):
    def __init__(self, url: str):
        self.url = url

    def load(self) -> pd.DataFrame:
        response = requests.get(self.url)
        response.raise_for_status()

        reader = ipc.open_stream(pa.BufferReader(response.content))
        table = reader.read_all()
        return table.to_pandas()