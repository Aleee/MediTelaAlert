import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from mainwindowUI import Ui_MainWindow
from emulator import Emulator
from updater import Updater
from sqlwrapper import PrivateDbConsts, clear_db_table
from customobjects.QSqlTableModel import CustomSqlTableModel
from customobjects.QGroupBox import GroupBoxWithRadiobuttons
from customobjects.QCheckBox import BuddyCheckBox
import lovely_logger as log
from typing import Union
from notifier import Notifier


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.settings = QSettings()
        self.db_consts: [PrivateDbConsts, None] = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Трекер приемного отделения")
        self.set_connections()
        self.initialize_cusstom_widgets()

        self.con_p: Union[QSqlDatabase, None] = None
        self.establish_connection()

        for table in [
            "patientinfo",
            "statusinfo",
        ]:
            clear_db_table(table, self.con_p)

        self.sqlmodel: Union[CustomSqlTableModel, None] = None
        self.ui.tv.setModel(self.create_model())
        self.ui.tv.connect_sidewidget(self.ui.sidewdg)
        self.ui.tv.set_private_connections()
        self.ui.tv.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tv.horizontalHeader().setMinimumSectionSize(5)
        self.ui.tv.pass_db_consts(self.db_consts)
        self.notifier = Notifier(log_wdg=self.ui.te_log)

        time.sleep(0.5)
        # run emulator
        self.emulator = Emulator()
        self.thread_2 = QThread()
        self.emulator.moveToThread(self.thread_2)
        self.thread_2.started.connect(self.emulator.emulate)
        self.thread_2.start()
        time.sleep(0.5)
        # run updater
        self.updater = Updater(private_connection=self.con_p,
                               private_db_consts=self.db_consts,
                               sqlmodel=self.sqlmodel,
                               notifier=self.notifier)
        self.updater.run()

        self.ui.tv.reformat_tableview(initialization=True)
        self.set_filter()
        self.connect_chbs_to_tv(self.ui.tv)

    def establish_connection(self):
        self.con_p = QSqlDatabase.addDatabase("QSQLITE",
                                              connectionName="private_mainthread")
        self.con_p.setDatabaseName("db.db")
        self.con_p.open()
        self.db_consts = PrivateDbConsts()

    def set_connections(self):
        self.ui.pb_reload.clicked.connect(
            lambda: self.updater.force_update(self.ui.pb_reload))
        for chb in self.ui.gb_filter.findChildren(QCheckBox):
            chb.stateChanged.connect(self.set_filter)

    def initialize_cusstom_widgets(self):
        for widget in self.ui.centralwidget.findChildren(GroupBoxWithRadiobuttons):
            widget.initialize()

    def set_filter(self):
        selected_rooms = "room IN ("
        for chb in self.ui.gb_filter.findChildren(QCheckBox):
            if chb.isChecked():
                selected_rooms += ("\'" + chb.objectName().split('_')[2] + "\',")
        filtered = (selected_rooms[:-1] if selected_rooms[-1] == ","
                    else selected_rooms) + ")"
        self.ui.tv.model().setFilter(filtered)

    def create_model(self) -> CustomSqlTableModel:
        self.sqlmodel = CustomSqlTableModel(db=self.con_p, db_consts=self.db_consts)
        self.sqlmodel.setTable("patientinfo")
        self.sqlmodel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlmodel.select()
        return self.sqlmodel

    def connect_chbs_to_tv(self, tableview: QTableView):
        for chb in self.ui.sidewdg.findChildren(BuddyCheckBox):
            chb.connect_tableview(tableview)
            chb.set_sql_connection(self.con_p)


if __name__ == '__main__':
    log.init('filename.log')
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
