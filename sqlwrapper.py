from PyQt5.QtSql import *
import lovely_logger
from dataclasses import dataclass
from methods import get_number_of_init_columns, get_number_of_instr_columns, \
    get_number_of_lab_columns, get_column_number_from_name


@dataclass()
class PrivateDbConsts:
    init_cols_number: int = get_number_of_init_columns()
    lab_cols_number: int = get_number_of_lab_columns()
    instr_cols_number: int = get_number_of_instr_columns()
    col_room: int = get_column_number_from_name("room")
    col_time_text: int = get_column_number_from_name("time_text")


def process_query(query: QSqlQuery) -> bool:
    if not query.exec():
        lovely_logger.e(f"{query.lastQuery().split(' ', 1)[0]} query "
                        f"(\"{query.lastQuery()}\") "
                        f"failed with error: {query.lastError().text()}")
        return False
    else:
        return True


def clear_db_table(tablename: str, sqlconnection: QSqlDatabase) -> bool:
    query = QSqlQuery(f"DELETE FROM {tablename}", db=sqlconnection)
    return process_query(query)
