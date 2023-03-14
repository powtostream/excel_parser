from handler import Handler
from db_connector import DbConnector


def app_run():
    print('Starting excel parser')
    file_path = "Приложение_к_заданию_бек_разработчика.xlsx"
    db_name = "test.db"
    db_connector = DbConnector(db_name)
    with open('sql_scripts/create_table.sql', 'r') as sql:
        db_connector.execute(sql.read())
    handler = Handler()
    handler.parse_xlsx(file_path, db_name)
    print('Parsing finished')


if __name__ == "__main__":
    app_run()
