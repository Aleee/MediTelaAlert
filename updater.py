from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from sqlwrapper import process_query, PrivateDbConsts
from consts import SQL_INSERTDATA, SQL_UPDATEDATA
import random
from typing import Union
from methods import str_to_int
from notifier import Notifier


class Updater(QObject):

    def __init__(self,
                 private_connection: QSqlDatabase,
                 private_db_consts: PrivateDbConsts,
                 sqlmodel: QSqlTableModel,
                 notifier: Notifier):
        super(Updater, self).__init__()
        self.con_f: Union[QSqlDatabase, None] = None
        self.con_p = private_connection
        self.db_consts = private_db_consts
        self.sqlmodel = sqlmodel
        self.notifier = notifier
        self.timer = QTimer()
        self.time_since_last_upd = 0
        self.settings = QSettings("settings.ini", QSettings.IniFormat)

    def run(self):
        self.con_f = QSqlDatabase.addDatabase("QSQLITE",
                                              connectionName="foreign_updater")
        self.con_f.setDatabaseName("fakedb.db")
        self.con_f.open()

        self.update_privatedb()
        self.timer.timeout.connect(self.check_update_needed)
        self.timer.start(10000)

    def check_update_needed(self):
        self.time_since_last_upd += 10000
        autorefresh_threshold = str_to_int(self.settings.value("autorefresh"))
        if autorefresh_threshold:
            if self.time_since_last_upd >= autorefresh_threshold:
                self.time_since_last_upd = 0
                self.update_privatedb()

    def force_update(self, button: QPushButton):
        button.setEnabled(False)
        if self.update_privatedb():
            self.time_since_last_upd = 0
            self.timer.start(10000)
        button.setEnabled(True)

    def update_privatedb(self) -> bool:
        # Get values from foreign DB

        data_emergdept = {}
        query = QSqlQuery(db=self.con_f)
        query.prepare("SELECT * FROM emergdept")
        query.exec()
        while query.next():
            data_emergdept[query.value(1)] = (query.value(2), query.value(3))

        data_patient = {}
        query.prepare("SELECT * FROM patient")
        query.exec()
        while query.next():
            data_patient[query.value(0)] = (query.value(1), query.value(2))

        data_labtest = []
        query.prepare("SELECT * FROM labtest")
        query.exec()
        while query.next():
            data_labtest.append((query.value(0), query.value(1), query.value(2),
                                 query.value(3), query.value(4)))

        data_instrtest = []
        query.prepare("SELECT * FROM instrtest")
        query.exec()
        while query.next():
            data_instrtest.append((query.value(0), query.value(1), query.value(2),
                                   query.value(3), query.value(4)))

        # Update private DB

        query = QSqlQuery(db=self.con_p)
        query_storeddata = QSqlQuery(db=self.con_p)
        for patient_id in data_emergdept.keys():
            query_storeddata.prepare("SELECT * FROM patientinfo WHERE patient_id = ?")
            query_storeddata.addBindValue(patient_id)
            process_query(query_storeddata)
            # Если запись для этого пациента уже имеется
            if query_storeddata.next() and query_storeddata.value(0):
                query.prepare(SQL_UPDATEDATA)
                query.addBindValue(data_emergdept[patient_id][1])  # room
                for labtest_type in range(1, self.db_consts.lab_cols_number // 3 + 1):
                    is_present = False
                    for labtest_entry in data_labtest:
                        if not is_present and labtest_entry[1] == patient_id and \
                                labtest_entry[3] == labtest_type:
                            query.addBindValue(labtest_entry[4])  # статус
                            query.addBindValue(labtest_entry[2])  # время
                            # Если статус поменялся и включено отслеживание
                            status_changed = query_storeddata.value(
                                ((labtest_type - 1) * 3) + self.db_consts.init_cols_number) != labtest_entry[4]
                            follow_enabled = query_storeddata.value(
                                ((labtest_type - 1) * 3) + self.db_consts.init_cols_number + 2) == 1
                            if status_changed and follow_enabled:
                                query.addBindValue(1)
                                self.notifier.add_alert(patient_id=patient_id,
                                                        patient_name=query_storeddata.value(1),
                                                        test_type="lab",
                                                        test_id=labtest_type,
                                                        new_status=labtest_entry[4],
                                                        time=labtest_entry[2])
                            else:
                                query.addBindValue(
                                    query_storeddata.value(
                                        ((labtest_type - 1) * 3) + self.db_consts.init_cols_number + 2))
                            is_present = True
                    if not is_present:
                        query.addBindValue(None)
                        query.addBindValue(None)
                        query.addBindValue(
                            query_storeddata.value(((labtest_type - 1) * 3) + self.db_consts.init_cols_number + 2))

                for instrtest_type in range(1, self.db_consts.instr_cols_number // 3 + 1):
                    is_present = False
                    for instrtest_entry in data_instrtest:
                        if not is_present and instrtest_entry[1] == patient_id and \
                                instrtest_entry[3] == instrtest_type:
                            query.addBindValue(instrtest_entry[4])  # статус
                            query.addBindValue(instrtest_entry[2])  # время
                            # Если статус поменялся и включено отслеживание
                            status_changed = query_storeddata.value(
                                ((instrtest_type - 1) * 3) + self.db_consts.init_cols_number + self.db_consts.lab_cols_number) != instrtest_entry[4]
                            follow_enabled = query_storeddata.value(
                                ((instrtest_type - 1) * 3) + self.db_consts.init_cols_number + self.db_consts.lab_cols_number + 2) == 1
                            if status_changed and follow_enabled:
                                query.addBindValue(2)
                            # Иначе
                            else:
                                query.addBindValue(
                                    query_storeddata.value(
                                        ((instrtest_type - 1) * 3) + self.db_consts.init_cols_number + self.db_consts.lab_cols_number + 2))
                            is_present = True
                    if not is_present:
                        query.addBindValue(None)
                        query.addBindValue(None)
                        query.addBindValue(
                            query_storeddata.value(((instrtest_type - 1) * 3) + self.db_consts.init_cols_number + self.db_consts.lab_cols_number + 2))

                query.addBindValue(patient_id)

                process_query(query=query)

            # Если записи для этого пациента нет
            else:
                query.prepare(SQL_INSERTDATA)
                query.addBindValue(patient_id)  # id
                query.addBindValue(data_patient[patient_id][0])  # name
                query.addBindValue(data_emergdept[patient_id][1])  # room
                query.addBindValue(data_emergdept[patient_id][0])  # time_text
                query.addBindValue(data_emergdept[patient_id][0])  # time_numeric
                query.addBindValue(data_patient[patient_id][1])  # birthdate

                for labtest_type in range(1, self.db_consts.lab_cols_number // 3 + 1):
                    is_present = False
                    for labtest_entry in data_labtest:
                        if not is_present and labtest_entry[1] == patient_id and \
                                labtest_entry[3] == labtest_type:
                            query.addBindValue(labtest_entry[4])
                            query.addBindValue(labtest_entry[2])
                            query.addBindValue(random.choice([0, 1]))  # temprorary
                            is_present = True
                    if not is_present:
                        query.addBindValue(None)
                        query.addBindValue(None)
                        query.addBindValue(None)

                for instrtest_type in range(1, self.db_consts.instr_cols_number // 3 + 1):
                    is_present = False
                    for instrtest_entry in data_instrtest:
                        if not is_present and instrtest_entry[1] == patient_id and \
                                instrtest_entry[3] == instrtest_type:
                            query.addBindValue(instrtest_entry[4])
                            query.addBindValue(instrtest_entry[2])
                            query.addBindValue(random.choice([0, 1]))  # temprorary
                            is_present = True
                    if not is_present:
                        query.addBindValue(None)
                        query.addBindValue(None)
                        query.addBindValue(None)

            if not process_query(query=query):
                return False

        self.notifier.push_notifications()
        self.sqlmodel.select()
        return True
