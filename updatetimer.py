from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *


class TableUpdateTimer:
    def __init__(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.action_on_timeout)

        self.update_interval = 0

    def get_duration_setting(self):
        return self.setting_wdg.get_checked_button_property("duration")

    def start(self, duration):
        pass

    def action_on_timeout(self):
        pass

DURATION_INT = 0

def timer_start(self):
    self.time_left_int = DURATION_INT

    self.my_qtimer = QTimer(self)
    self.my_qtimer.timeout.connect(self.timer_timeout)
    self.my_qtimer.start(1000)

    self.update_gui()


def timer_timeout(self):
    self.time_left_int -= 1

    if self.time_left_int == 0:
        self.widget_counter_int = (self.widget_counter_int + 1) % 4
        self.pages_qsw.setCurrentIndex(self.widget_counter_int)
        self.time_left_int = DURATION_INT

    self.update_gui()


def update_gui(self):
    self.time_passed_qll.setText(str(self.time_left_int))