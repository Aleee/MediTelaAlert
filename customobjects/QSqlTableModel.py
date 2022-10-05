from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from datetime import datetime
import humanize
from consts import DATETIME_F, SYMBOLS
from sqlwrapper import PrivateDbConsts


class CustomSqlTableModel(QSqlTableModel):
    def __init__(self, db, db_consts):
        super(CustomSqlTableModel, self).__init__(db=db)
        self.db_consts: PrivateDbConsts = db_consts
        humanize.activate("ru_RU")

    def find_column_by_sql_columnname(self, name: str):
        for column in range(self.columnCount()):
            if self.headerData(column, Qt.Horizontal, Qt.UserRole) == name:
                return column
        return None

    def data(self, index: QModelIndex, role=None):
        value = super(CustomSqlTableModel, self).data(index, Qt.DisplayRole)

        if role == Qt.DisplayRole and index.column() == self.db_consts.col_time_text:
            adm_datetime = datetime.strptime(value, DATETIME_F)
            curr_datetime = datetime.now()
            delta = curr_datetime - adm_datetime
            return " " + humanize.precisedelta(delta, minimum_unit="minutes",
                                               format="%0d")
        if role == Qt.TextAlignmentRole:
            if index.column() >= self.db_consts.init_cols_number or index.column() == self.db_consts.col_room:
                return Qt.AlignCenter
        if role == Qt.ForegroundRole and index.column() >= self.db_consts.init_cols_number:
            if value == 1:
                return QColor(QRgba64().fromRgba(205, 0, 0, 255))
            elif value in [2, 3]:
                return QColor(QRgba64().fromRgba(215, 180, 0, 255))
            elif value == 4:
                return QColor(QRgba64().fromRgba(190, 210, 0, 255))
            elif value == 5:
                return QColor(QRgba64().fromRgba(0, 125, 60, 255))
            elif value in [6, 7]:
                return QColor(QRgba64().fromRgba(165, 0, 165, 255))
        if (role == Qt.BackgroundRole and
                index.column() >= self.db_consts.init_cols_number and
                index.column() % 3 == self.db_consts.init_cols_number % 3):
            if index.siblingAtColumn(index.column() + 2).data(Qt.DisplayRole):
                return QColor(QRgba64().fromRgba(215, 215, 255, 100))
        if role == Qt.FontRole and index.column() >= self.db_consts.init_cols_number:
            if value == 1:
                return QFont("Times", 7, QFont.Bold)
            elif value in [5, 6, 7]:
                return QFont("Times", 20, QFont.Bold)
            else:
                return QFont("Times", 12, QFont.Bold)
        if role == Qt.UserRole \
                and index.column() >= self.db_consts.init_cols_number \
                and index.column() % 3 == self.db_consts.init_cols_number % 3:
            return value
        if role == Qt.DisplayRole and index.column() >= self.db_consts.init_cols_number:
            if value in range(1, 5):
                return SYMBOLS["in_progress"]
            elif value == 5:
                return SYMBOLS["done"]
            elif value in [6, 7]:
                return SYMBOLS["cancelled"]
        if role == Qt.ToolTipRole and index.column() >= self.db_consts.init_cols_number:
            update_datetime = self.data(index.siblingAtColumn(index.column() + 1),
                                        Qt.DisplayRole)
            if update_datetime:
                delta = datetime.now() - datetime.strptime(update_datetime, DATETIME_F)
                return ("Последнее обновление:\n" +
                        humanize.precisedelta(delta,
                                              minimum_unit="minutes",
                                              format="%0d") +
                        " назад")
            else:
                return ""

        return super(CustomSqlTableModel, self).data(index, role)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        if index.column() >= self.db_consts.init_cols_number:
            return Qt.NoItemFlags
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
