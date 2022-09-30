from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from typing import Union
from consts import TV_HEADERS
from customobjects.QCheckBox import BuddyCheckBox


class CustomTableView(QTableView):
    def __init__(self, parentwdg: QWidget = None):
        super(CustomTableView, self).__init__(parentwdg)
        self.sidewidget: Union[QWidget, None] = None

    def connect_sidewidget(self, sidewidget: QWidget):
        self.sidewidget = sidewidget
        self.sidewidget_set_visible(False)
        self.selectionModel().selectionChanged.connect(self.handle_selection)

    def sqlcolumnname_by_index(self, index) -> str:
        return self.model().headerData(index.column(), Qt.Horizontal, Qt.UserRole)

    def reformat_tableview(self, initialization: bool = False):
        for column, settings in TV_HEADERS.items():
            if initialization:
                self.model().setHeaderData(column,
                                           Qt.Horizontal,
                                           settings[0],
                                           role=Qt.DisplayRole)
                self.model().setHeaderData(column,
                                           Qt.Horizontal,
                                           settings[3],
                                           role=Qt.UserRole)
                self.setColumnWidth(column, settings[1])
                if settings[2] == 0:
                    self.hideColumn(column)

                p = QPalette()
                p.setColor(QPalette.Highlight, QColor("red"))
                p.setColor(QPalette.HighlightedText, QColor("blue"))
                # self.setPalette(p)

            if settings[2] == 2:
                for row in range(self.model().rowCount()):
                    curr_index = self.model().index(row, column)
                    if (self.model().data(curr_index,
                                          Qt.DisplayRole) or
                            self.model().data(curr_index.siblingAtColumn(column + 2),
                                              Qt.DisplayRole)):
                        self.showColumn(column)
                        break
                else:
                    self.hideColumn(column)

    def sidewidget_set_visible(self, visibility: bool):
        if self.sidewidget:
            for wdg in self.sidewidget.findChildren((QFrame, QLabel, BuddyCheckBox)):
                wdg.setVisible(visibility)

    def data_from_selection_sibling(self, selection: QItemSelection, column: int,
                                    role=Qt.DisplayRole):
        return self.model().data(selection.indexes()[0].siblingAtColumn(column), role)

    @pyqtSlot(QItemSelection, QItemSelection)
    def handle_selection(self, selection: QItemSelection, deselection: QItemSelection):
        # Отображение виджета
        self.sidewidget_set_visible(bool(selection.indexes()))
        if selection.indexes():
            # Смена имени и даты рождения
            self.sidewidget.findChild(QLabel, name="la_name").setText(
                self.data_from_selection_sibling(selection, 1))
            self.sidewidget.findChild(QLabel, name="la_birthdate").setText(
                self.data_from_selection_sibling(selection, 70))
            # Установка чекбоксов
            for column in range(22):
                follow = self.data_from_selection_sibling(selection, 6 + column * 3)
                col_name: str = self.model().headerData(6 + column * 3, Qt.Horizontal,
                                                        Qt.UserRole)
                chb_name = "chb_" + col_name.split("_", 1)[0]
                self.sidewidget.findChild(BuddyCheckBox, name=chb_name).setChecked(
                    bool(follow))
