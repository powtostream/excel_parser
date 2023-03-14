from db_connector import DbConnector
from loader import Loader


class Handler(object):

    @staticmethod
    def _get_dataframe(file_path):
        data_frame = Loader(file_path).load_pandas_df(
            header_levels=[0, 1, 2], index_columns=[0, 1]
        )
        return data_frame

    def parse_xlsx(self, file_path, db_name):
        data_frame = self._get_dataframe(file_path)
        data_frame = data_frame.swaplevel(0, 1, 1)
        data_frame = data_frame.stack().stack().reset_index()
        data_frame = data_frame.drop(columns=['level_0'])
        data_frame = data_frame.rename(columns={
            'level_1': 'company', 'level_2': 'date', 'company': 'calc_type'
        })
        data_frame = data_frame.replace(
            {'date': {'data1': '2023-03-13', 'data2': '2023-03-14'}}
        )
        values_list = data_frame.values.tolist()
        values_tuples = list()

        for row in values_list:
            values_tuples.append(tuple(row))

        db_connector = DbConnector(db_name)
        db_connector.insert_values(values_tuples)

        grouped = (
            data_frame
            .groupby(['date', 'calc_type'])[['Qliq', 'Qoil']]
            .sum()
            .reset_index()
        )
        forecast_data = grouped[grouped['calc_type'] == 'forecast']
        print(forecast_data)
