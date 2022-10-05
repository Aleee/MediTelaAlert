from PyQt5.QtCore import *
from PyQt5.QtSql import *
import time
import random
from typing import Union
from datetime import datetime, timedelta
from sqlwrapper import process_query, clear_db_table
from consts import NAMES, DATETIME_F


class Emulator(QObject):
    
    def __init__(self):
        super(Emulator, self).__init__()
        self.con_f: Union[QSqlDatabase, None] = None

    def emulate(self):
        self.establish_sqlconnection()
        self.clean_tables()
        self.create_starting_pos()
        self.emulate_changes()

    def establish_sqlconnection(self):
        self.con_f = QSqlDatabase.addDatabase("QSQLITE",
                                              connectionName="foreign_emulatorthread")
        self.con_f.setDatabaseName("fakedb.db")
        self.con_f.open()

    def clean_tables(self):
        for table in [
            "emergdept",
            "emergexam",
            "instrtest",
            "labtest",
            "patient",
        ]:
            clear_db_table(table, self.con_f)

    def create_starting_pos(self):
        # Пациенты
        query = QSqlQuery(self.con_f)
        query.prepare("INSERT INTO patient (name, birthdate) "
                      "VALUES (?, ?), (?, ?), (?, ?), (?, ?), (?, ?), (?, ?), (?, ?)")
        for i in random.sample(range(0, 300), 7):
            query.addBindValue(NAMES[i])
            query.addBindValue(str(random.randint(10, 28)) 
                               + ".0" + str(random.randint(1, 9)) 
                               + "." + str(random.randint(1950, 2000)) 
                               + "")
        process_query(query)
        last_inserted_id = query.lastInsertId()

        current_datetime = datetime.now()
        query = QSqlQuery(self.con_f)
        for patient_id in range(last_inserted_id - 6, last_inserted_id + 1):
            # Пребывание в приемном отеделении
            query.prepare("INSERT INTO emergdept (patient_id, admtime, room) "
                          "VALUES (?, ?, ?)")
            query.addBindValue(patient_id)
            delta = timedelta(minutes=random.randint(25, 120))
            admission_time = current_datetime - delta
            query.addBindValue(admission_time.strftime(DATETIME_F))
            query.addBindValue(random.choice(["7", "9", "T", "X"]))
            process_query(query)
            # Лабораторные исследования
            for lab_test_type in random.sample(range(1, 8), random.randint(1, 5)):
                query.prepare("INSERT INTO labtest "
                              "(patient_id, datetime, test_type, status) "
                              "VALUES (?, ?, ?, ?)")
                query.addBindValue(patient_id)
                delta = timedelta(minutes=random.randint(2, 24))
                query.addBindValue((admission_time + delta).strftime(DATETIME_F))
                query.addBindValue(lab_test_type)
                query.addBindValue(random.choice([1, 1, 2, 2, 4, 4, 4, 4, 4, 5]))
                process_query(query)
            # Инструментальные исследования
            for instr_test_type in random.sample(range(1, 4), random.randint(0, 2)):
                query.prepare("INSERT INTO instrtest "
                              "(patient_id, datetime, test_type, status) "
                              "VALUES (?, ?, ?, ?)")
                query.addBindValue(patient_id)
                delta = timedelta(minutes=random.randint(2, 24))
                query.addBindValue((admission_time + delta).strftime(DATETIME_F))
                query.addBindValue(instr_test_type)
                query.addBindValue(random.choice([1, 3, 5]))
                process_query(query)

    def emulate_changes(self):
        while not self.thread().isInterruptionRequested():
            time.sleep(9)
            query = QSqlQuery(self.con_f)
            # labtests
            query.prepare("UPDATE labtest SET status = status + 1, datetime = ? "
                          "WHERE test_type = ? AND status BETWEEN 1 AND 4")
            query.addBindValue(datetime.now().strftime(DATETIME_F))
            query.addBindValue(random.randint(1, 7))
            process_query(query)
            # instrtest
            query.prepare("UPDATE instrtest SET status = 5, datetime = ? "
                          "WHERE test_type = ? AND status IN (1, 3)")
            query.addBindValue(datetime.now().strftime(DATETIME_F))
            query.addBindValue(random.randint(1, 3))
            process_query(query)
