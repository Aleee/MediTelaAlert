from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from methods import str_to_int, get_custom_property


class GroupBoxWithRadiobuttons(QGroupBox):
    def __init__(self, parentwdg: QWidget):
        super(GroupBoxWithRadiobuttons, self).__init__(parentwdg)
        self.settings = QSettings("settings.ini", QSettings.IniFormat)

    def initialize(self):
        for button in self.findChildren(QRadioButton):
            if str_to_int(self.settings.value(get_custom_property(button)[0])) == get_custom_property(button)[1]:
                button.setChecked(True)
            button.clicked.connect(self.change_setting)

    @pyqtSlot(bool)
    def change_setting(self, is_checked):
        if is_checked:
            self.settings.setValue(*get_custom_property(self.sender()))


class GroupBoxWithCheckboxes(QGroupBox):
    def __init__(self, parentwdg: QWidget):
        super(GroupBoxWithCheckboxes, self).__init__(parentwdg)
        self.settings = QSettings("settings.ini", QSettings.IniFormat)

    def initialize(self):
        for button in self.findChildren(QRadioButton):
            if str_to_int(self.settings.value(button.property("property"))) == button.property("value"):
                button.setChecked(True)
            button.clicked.connect(self.change_setting)

    @pyqtSlot(bool)
    def change_setting(self, is_checked):
        if is_checked:
            self.settings.setValue(*get_custom_property(self.sender()))