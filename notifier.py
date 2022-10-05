from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from methods import str_to_int
from dataclasses import dataclass
from typing import List
from datetime import datetime
from consts import DATETIME_F_SHORT, LABTESTS, LOG_MSG, WIN_MSG
from plyer import notification as pl_notification
from customobjects.QDialog import NotificationDialog


@dataclass
class Notification:
    patient_id: int
    patient_name: str
    test_type: str
    test_id: int
    new_status: int
    time: str


class Notifier:
    def __init__(self, log_wdg: QTextEdit):
        self.log_wdg: QTextEdit = log_wdg
        self.saved_text: str = ""
        self.pending_notifications: List[Notification] = []
        self.settings = QSettings("settings.ini",
                                  QSettings.IniFormat)
        self.dialogues = []

    def add_alert(self,
                  patient_id: str,
                  patient_name: str,
                  test_type: str,
                  test_id: int,
                  new_status: str,
                  time: str):
        new_notification = Notification(str_to_int(patient_id),
                                        patient_name,
                                        test_type,
                                        test_id,
                                        str_to_int(new_status),
                                        time)
        if (new_notification.patient_id
                and new_notification.new_status):
            self.pending_notifications.append(new_notification)

    def push_notifications(self):
        verbosity = str_to_int(self.settings.value("verbosity"))
        for note in self.pending_notifications:
            if note.new_status == 5:
                if verbosity > 0:
                    self.log_wdg.append(self.make_log_message(note))
                if verbosity == 2:
                    self.send_win_notification(note)
                if verbosity == 3:
                    self.create_popup_window(note)
        self.pending_notifications.clear()

    @staticmethod
    def make_log_message(note: Notification):
        return LOG_MSG.format(datetime.now().strftime(DATETIME_F_SHORT),
                              LABTESTS[note.test_id],
                              note.patient_name,
                              note.time)

    @staticmethod
    def make_win_notification_message(note: Notification):
        return LABTESTS[note.test_id], \
               WIN_MSG.format(LABTESTS[note.test_id], note.patient_name)

    def send_win_notification(self, note: Notification):
        title, msg = self.make_win_notification_message(note)
        pl_notification.notify(title=title,
                               message=msg,
                               timeout=120)

    def create_popup_window(self, note):
        dialog = NotificationDialog(note=note)
        self.dialogues.append(dialog)
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()
