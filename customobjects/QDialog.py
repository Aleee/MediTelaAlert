from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from consts import LABTESTS


class NotificationDialog(QDialog):
    def __init__(self, note):
        super().__init__(flags=Qt.Dialog)

        self.note = note

        self.setModal(True)
        self.setWindowTitle("Приемное отделение")

        self.setFixedWidth(300)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(f"Время: {self.note.time}"), alignment=Qt.AlignLeft)
        self.layout.addWidget(QLabel(f"Пациент: {self.note.patient_name}"), alignment=Qt.AlignLeft)
        self.layout.addWidget(QLabel(f"Исследование: {LABTESTS[self.note.test_id]}"), alignment=Qt.AlignLeft)
        self.layout.addWidget(QLabel(f"Статус: ГОТОВО"), alignment=Qt.AlignLeft)
        self.layout.addWidget(QLabel(f""), alignment=Qt.AlignLeft)
        self.layout.addWidget(self.buttonBox, alignment=Qt.AlignRight)
        self.setLayout(self.layout)
