from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from typing import Union
from consts import TV_HEADERS
from customobjects.QCheckBox import BuddyCheckBox
from methods import get_column_number_from_name
from sqlwrapper import PrivateDbConsts


class CustomTableView(QTableView):
    def __init__(self, parentwdg: QWidget = None):
        super(CustomTableView, self).__init__(parentwdg)
        self.sidewidget: Union[QWidget, None] = None
        self.db_consts: Union[PrivateDbConsts, None] = None

        self.selection = None

    def connect_sidewidget(self, sidewidget: QWidget):
        self.sidewidget = sidewidget
        self.sidewidget_set_visible(False)
        self.selectionModel().selectionChanged.connect(self.handle_selection)

    def set_private_connections(self):
        self.model().modelAboutToBeReset.connect(self.save_selection)
        self.model().modelReset.connect(self.restore_selection)

    def save_selection(self):
        self.selection = self.selectionModel().selectedIndexes()

    def restore_selection(self):
        try:
            selection_index = self.selection[0]
            self.selectionModel().select(selection_index, QItemSelectionModel.ClearAndSelect)
            self.selectRow(selection_index.row())
            self.handle_selection(QItemSelection(selection_index, selection_index), QItemSelection())
        except IndexError:
            pass

    def pass_db_consts(self, db_consts_container: PrivateDbConsts):
        self.db_consts = db_consts_container

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
                self.data_from_selection_sibling(selection, get_column_number_from_name("name")))
            self.sidewidget.findChild(QLabel, name="la_birthdate").setText(
                self.data_from_selection_sibling(selection, get_column_number_from_name("birthdate")))
            # Установка чекбоксов
            for column in range(0, (self.db_consts.lab_cols_number + self.db_consts.instr_cols_number) // 3):
                follow = self.data_from_selection_sibling(selection, self.db_consts.init_cols_number + column * 3 + 2)
                col_name: str = self.model().headerData(self.db_consts.init_cols_number + column * 3, Qt.Horizontal,
                                                        Qt.UserRole)
                chb_name = "chb_" + col_name.split("_", 1)[0]
                chb_widget = self.sidewidget.findChild(BuddyCheckBox, name=chb_name)
                chb_widget.setChecked(bool(follow))
                chb_widget.change_color(chb_widget.checkState())
