from PyQt5.QtSql import *
from PyQt5.QtCore import *
from sqlwrapper import process_query
from consts import SQL_INSERTDATA, SQL_UPDATEDATA
import random
import time
from typing import Union


class Updater(QObject):

    def __init__(self):
        super(Updater, self).__init__()
        self.con_f: Union[QSqlDatabase, None] = None
        self.con_p: Union[QSqlDatabase, None] = None

    def update(self):
        self.con_f = QSqlDatabase.addDatabase("QSQLITE",
                                              connectionName="foreign_updatethread")
        self.con_f.setDatabaseName("fakedb.db")
        self.con_f.open()
        self.con_p = QSqlDatabase.addDatabase("QSQLITE",
                                              connectionName="private_updatethread")
        self.con_p.setDatabaseName("db.db")
        self.con_p.open()

        while not self.thread().isInterruptionRequested():
            if self.update_privatedb():
                time.sleep(30)

    def update_privatedb(self):
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
                for labtest_type in range(1, 13):
                    is_present = False
                    for labtest_entry in data_labtest:
                        if not is_present and labtest_entry[1] == patient_id and \
                                labtest_entry[3] == labtest_type:
                            query.addBindValue(labtest_entry[4])  # статус
                            query.addBindValue(labtest_entry[2])  # время
                            # Если статус поменялся и включено отслеживание
                            status_changed = query_storeddata.value(
                                ((labtest_type - 1) * 3) + 4) != labtest_entry[4]
                            follow_enabled = query_storeddata.value(
                                ((labtest_type - 1) * 3) + 6) == 1
                            if status_changed and follow_enabled:
                                query.addBindValue(2)
                            else:
                                query.addBindValue(
                                    query_storeddata.value(
                                        ((labtest_type - 1) * 3) + 6))
                            is_present = True
                    if not is_present:
                        query.addBindValue(None)
                        query.addBindValue(None)
                        query.addBindValue(
                            query_storeddata.value(((labtest_type - 1) * 3) + 6))

                for instrtest_type in range(1, 5):
                    is_present = False
                    for instrtest_entry in data_instrtest:
                        if not is_present and instrtest_entry[1] == patient_id and \
                                instrtest_entry[3] == instrtest_type:
                            query.addBindValue(instrtest_entry[4])  # статус
                            query.addBindValue(instrtest_entry[2])  # время
                            # Если статус поменялся и включено отслеживание
                            status_changed = query_storeddata.value(
                                ((instrtest_type - 1) * 3) + 40) != instrtest_entry[4]
                            follow_enabled = query_storeddata.value(
                                ((instrtest_type - 1) * 3) + 42) == 1
                            if status_changed and follow_enabled:
                                query.addBindValue(2)
                            # Иначе
                            else:
                                query.addBindValue(
                                    query_storeddata.value(
                                        ((instrtest_type - 1) * 3) + 42))
                            is_present = True
                    if not is_present:
                        query.addBindValue(None)
                        query.addBindValue(None)
                        query.addBindValue(
                            query_storeddata.value(((instrtest_type - 1) * 3) + 42))

                for exam in range(1, 19):
                    query.addBindValue(None)

                query.addBindValue(patient_id)

                process_query(query=query)

            # Если записи для этого пациента нет
            else:
                query.prepare(SQL_INSERTDATA)
                query.addBindValue(patient_id)  # 0
                query.addBindValue(data_patient[patient_id][0])  # 1
                query.addBindValue(data_emergdept[patient_id][1])  # 2
                query.addBindValue(data_emergdept[patient_id][0])  # 3

                for labtest_type in range(1, 13):
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

                for instrtest_type in range(1, 5):
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

                for exam in range(1, 19):
                    query.addBindValue(None)

                # дата рождения
                query.addBindValue(data_patient[patient_id][1])

            process_query(query=query)
