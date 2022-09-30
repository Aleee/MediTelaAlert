from PyQt5.QtSql import *
import lovely_logger


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
