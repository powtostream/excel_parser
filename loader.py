import pandas as pd


class Loader(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pandas_df(self, header_levels, index_columns):
        return pd.read_excel(
            self.file_path, header=header_levels, index_col=index_columns
        )
