from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from typing import Union
from sqlwrapper import process_query


class BuddyCheckBox(QCheckBox):
    def __init__(self, parentwdg: QWidget):
        super(BuddyCheckBox, self).__init__(parentwdg)
        self.tv = None
        self.con: Union[QSqlDatabase, None] = None
        self.clicked.connect(self.change_follow_status)
        self.stateChanged.connect(self.change_color)

    def connect_tableview(self, tableview) -> None:
        self.tv = tableview

    def set_sql_connection(self, con: QSqlDatabase) -> None:
        self.con = con

    @pyqtSlot()
    def change_follow_status(self) -> None:
        query = QSqlQuery(self.con)
        follow_column_name = self.objectName().split('_')[1] + '_follow'
        follow_column_value = int(self.isChecked())
        tv_current_row = self.tv.currentIndex().row()
        tv_current_patientid = self.tv.currentIndex().siblingAtColumn(0).data(Qt.DisplayRole)
        query.prepare(f"UPDATE patientinfo SET {follow_column_name} = ? WHERE patient_id = ?")
        query.addBindValue(follow_column_value)
        query.addBindValue(tv_current_patientid)
        if process_query(query):
            self.tv.model().selectRow(tv_current_row)
            self.tv.reformat_tableview(False)

    @pyqtSlot(int)
    def change_color(self, state: int) -> None:
        if state:
            column_name: str = self.objectName().split("_", 1)[1] + "_status"
            column_num: int = self.tv.model().find_column_by_sql_columnname(column_name)
            selection_index: QModelIndex = self.tv.selectionModel().currentIndex()
            status_value: Union[str, int, None] = self.tv.model().data(
                selection_index.siblingAtColumn(column_num),
                Qt.UserRole)
            if not status_value:
                self.setStyleSheet(
                    "background-color: rgba(215, 215, 255, 0.5);")  # blueish
            elif status_value == 1:
                self.setStyleSheet(
                    "background-color: rgba(255, 145, 215, 0.5);")  # red
            elif status_value in [2, 3, 4]:
                self.setStyleSheet(
                    "background-color: rgba(235, 255, 80, 0.5);")  # yellow
            elif status_value == 5:
                self.setStyleSheet(
                    "background-color: rgba(165, 245, 145, 0.5);")  # green
            elif status_value in [6, 7]:
                self.setStyleSheet(
                    "background-color: rgba(165, 0, 165, 0.5);")  # magenta
        else:
            self.setStyleSheet("")
