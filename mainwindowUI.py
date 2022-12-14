# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.te_log = QtWidgets.QTextEdit(self.centralwidget)
        self.te_log.setReadOnly(True)
        self.te_log.setObjectName("te_log")
        self.gridLayout_4.addWidget(self.te_log, 0, 0, 6, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 2, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setMinimumSize(QtCore.QSize(30, 25))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_4.addWidget(self.toolButton, 0, 2, 1, 1)
        self.pb_log_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pb_log_clear.setObjectName("pb_log_clear")
        self.gridLayout_4.addWidget(self.pb_log_clear, 5, 1, 1, 2)
        self.pb_log_restore = QtWidgets.QPushButton(self.centralwidget)
        self.pb_log_restore.setObjectName("pb_log_restore")
        self.gridLayout_4.addWidget(self.pb_log_restore, 4, 1, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_4, 3, 0, 1, 2)
        self.tv = CustomTableView(self.centralwidget)
        self.tv.setMinimumSize(QtCore.QSize(730, 400))
        self.tv.setMaximumSize(QtCore.QSize(16777215, 400))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tv.setFont(font)
        self.tv.setObjectName("tv")
        self.gridLayout.addWidget(self.tv, 1, 0, 1, 1)
        self.sidewdg = QtWidgets.QFrame(self.centralwidget)
        self.sidewdg.setEnabled(True)
        self.sidewdg.setMinimumSize(QtCore.QSize(305, 400))
        self.sidewdg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sidewdg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidewdg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidewdg.setObjectName("sidewdg")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sidewdg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.la_header = QtWidgets.QLabel(self.sidewdg)
        self.la_header.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.la_header.setFont(font)
        self.la_header.setAlignment(QtCore.Qt.AlignCenter)
        self.la_header.setObjectName("la_header")
        self.gridLayout_2.addWidget(self.la_header, 4, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chb_oam = BuddyCheckBox(self.sidewdg)
        self.chb_oam.setObjectName("chb_oam")
        self.gridLayout_3.addWidget(self.chb_oam, 8, 0, 1, 1)
        self.chb_bnp = BuddyCheckBox(self.sidewdg)
        self.chb_bnp.setObjectName("chb_bnp")
        self.gridLayout_3.addWidget(self.chb_bnp, 4, 2, 1, 1)
        self.chb_crd = BuddyCheckBox(self.sidewdg)
        self.chb_crd.setObjectName("chb_crd")
        self.gridLayout_3.addWidget(self.chb_crd, 5, 0, 1, 1)
        self.chb_xra = BuddyCheckBox(self.sidewdg)
        self.chb_xra.setEnabled(True)
        self.chb_xra.setObjectName("chb_xra")
        self.gridLayout_3.addWidget(self.chb_xra, 11, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.sidewdg)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 9, 0, 1, 3)
        self.chb_tni = BuddyCheckBox(self.sidewdg)
        self.chb_tni.setObjectName("chb_tni")
        self.gridLayout_3.addWidget(self.chb_tni, 4, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.sidewdg)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 11, 1, 2, 1)
        self.la_instr = QtWidgets.QLabel(self.sidewdg)
        self.la_instr.setEnabled(True)
        self.la_instr.setMinimumSize(QtCore.QSize(128, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.la_instr.setFont(font)
        self.la_instr.setAlignment(QtCore.Qt.AlignCenter)
        self.la_instr.setObjectName("la_instr")
        self.gridLayout_3.addWidget(self.la_instr, 10, 0, 1, 3)
        self.chb_abc = BuddyCheckBox(self.sidewdg)
        self.chb_abc.setEnabled(True)
        self.chb_abc.setObjectName("chb_abc")
        self.gridLayout_3.addWidget(self.chb_abc, 7, 2, 1, 1)
        self.la_lab = QtWidgets.QLabel(self.sidewdg)
        self.la_lab.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.la_lab.setFont(font)
        self.la_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.la_lab.setObjectName("la_lab")
        self.gridLayout_3.addWidget(self.la_lab, 1, 0, 1, 3)
        self.chb_usd = BuddyCheckBox(self.sidewdg)
        self.chb_usd.setObjectName("chb_usd")
        self.gridLayout_3.addWidget(self.chb_usd, 11, 2, 1, 1)
        self.chb_psp = BuddyCheckBox(self.sidewdg)
        self.chb_psp.setObjectName("chb_psp")
        self.gridLayout_3.addWidget(self.chb_psp, 5, 2, 1, 1)
        self.chb_cts = BuddyCheckBox(self.sidewdg)
        self.chb_cts.setObjectName("chb_cts")
        self.gridLayout_3.addWidget(self.chb_cts, 12, 0, 1, 1)
        self.chb_bak = BuddyCheckBox(self.sidewdg)
        self.chb_bak.setObjectName("chb_bak")
        self.gridLayout_3.addWidget(self.chb_bak, 3, 0, 1, 1)
        self.chb_end = BuddyCheckBox(self.sidewdg)
        self.chb_end.setObjectName("chb_end")
        self.gridLayout_3.addWidget(self.chb_end, 12, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.sidewdg)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 2, 1, 7, 1)
        self.chb_acb = BuddyCheckBox(self.sidewdg)
        self.chb_acb.setObjectName("chb_acb")
        self.gridLayout_3.addWidget(self.chb_acb, 3, 2, 1, 1)
        self.chb_ddm = BuddyCheckBox(self.sidewdg)
        self.chb_ddm.setCheckable(True)
        self.chb_ddm.setObjectName("chb_ddm")
        self.gridLayout_3.addWidget(self.chb_ddm, 6, 0, 1, 1)
        self.chb_glu = BuddyCheckBox(self.sidewdg)
        self.chb_glu.setObjectName("chb_glu")
        self.gridLayout_3.addWidget(self.chb_glu, 7, 0, 1, 1)
        self.chb_agc = BuddyCheckBox(self.sidewdg)
        self.chb_agc.setObjectName("chb_agc")
        self.gridLayout_3.addWidget(self.chb_agc, 6, 2, 1, 1)
        self.chb_oak = BuddyCheckBox(self.sidewdg)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chb_oak.setFont(font)
        self.chb_oak.setObjectName("chb_oak")
        self.gridLayout_3.addWidget(self.chb_oak, 2, 0, 1, 1)
        self.chb_dia = BuddyCheckBox(self.sidewdg)
        self.chb_dia.setObjectName("chb_dia")
        self.gridLayout_3.addWidget(self.chb_dia, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 5, 0, 1, 1)
        self.la_birthdate = QtWidgets.QLabel(self.sidewdg)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.la_birthdate.setFont(font)
        self.la_birthdate.setObjectName("la_birthdate")
        self.gridLayout_2.addWidget(self.la_birthdate, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 1)
        self.la_name = QtWidgets.QLabel(self.sidewdg)
        self.la_name.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.la_name.setFont(font)
        self.la_name.setObjectName("la_name")
        self.gridLayout_2.addWidget(self.la_name, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.sidewdg)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 10)
        self.gridLayout.addWidget(self.sidewdg, 1, 1, 1, 1)
        self.topwdg = QtWidgets.QFrame(self.centralwidget)
        self.topwdg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topwdg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topwdg.setObjectName("topwdg")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.topwdg)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gb_filter = QtWidgets.QGroupBox(self.topwdg)
        self.gb_filter.setObjectName("gb_filter")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gb_filter)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.chb_filter_7 = QtWidgets.QCheckBox(self.gb_filter)
        self.chb_filter_7.setChecked(True)
        self.chb_filter_7.setObjectName("chb_filter_7")
        self.gridLayout_6.addWidget(self.chb_filter_7, 0, 0, 1, 1)
        self.chb_filter_9 = QtWidgets.QCheckBox(self.gb_filter)
        self.chb_filter_9.setChecked(True)
        self.chb_filter_9.setObjectName("chb_filter_9")
        self.gridLayout_6.addWidget(self.chb_filter_9, 0, 1, 1, 1)
        self.chb_filter_T = QtWidgets.QCheckBox(self.gb_filter)
        self.chb_filter_T.setChecked(True)
        self.chb_filter_T.setObjectName("chb_filter_T")
        self.gridLayout_6.addWidget(self.chb_filter_T, 1, 0, 1, 1)
        self.chb_filter_X = QtWidgets.QCheckBox(self.gb_filter)
        self.chb_filter_X.setObjectName("chb_filter_X")
        self.gridLayout_6.addWidget(self.chb_filter_X, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.gb_filter, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 1, 1, 1)
        self.gb_notifytype = GroupBoxWithRadiobuttons(self.topwdg)
        self.gb_notifytype.setObjectName("gb_notifytype")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gb_notifytype)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.rb_notifytype_off = QtWidgets.QRadioButton(self.gb_notifytype)
        self.rb_notifytype_off.setProperty("value", 0)
        self.rb_notifytype_off.setObjectName("rb_notifytype_off")
        self.gridLayout_7.addWidget(self.rb_notifytype_off, 1, 1, 1, 1)
        self.rb_notifytype_log = QtWidgets.QRadioButton(self.gb_notifytype)
        self.rb_notifytype_log.setProperty("value", 1)
        self.rb_notifytype_log.setObjectName("rb_notifytype_log")
        self.gridLayout_7.addWidget(self.rb_notifytype_log, 0, 1, 1, 1)
        self.rb_notifytype_notification = QtWidgets.QRadioButton(self.gb_notifytype)
        self.rb_notifytype_notification.setChecked(True)
        self.rb_notifytype_notification.setProperty("value", 2)
        self.rb_notifytype_notification.setObjectName("rb_notifytype_notification")
        self.gridLayout_7.addWidget(self.rb_notifytype_notification, 1, 0, 1, 1)
        self.rb_notifytype_popup = QtWidgets.QRadioButton(self.gb_notifytype)
        self.rb_notifytype_popup.setProperty("value", 3)
        self.rb_notifytype_popup.setObjectName("rb_notifytype_popup")
        self.gridLayout_7.addWidget(self.rb_notifytype_popup, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.gb_notifytype, 0, 4, 1, 1)
        self.gb_refresh = GroupBoxWithRadiobuttons(self.topwdg)
        self.gb_refresh.setObjectName("gb_refresh")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gb_refresh)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.rb_refresh_05 = QtWidgets.QRadioButton(self.gb_refresh)
        self.rb_refresh_05.setChecked(False)
        self.rb_refresh_05.setProperty("value", 30000)
        self.rb_refresh_05.setObjectName("rb_refresh_05")
        self.gridLayout_8.addWidget(self.rb_refresh_05, 0, 0, 1, 1)
        self.rb_refresh_2 = QtWidgets.QRadioButton(self.gb_refresh)
        self.rb_refresh_2.setChecked(True)
        self.rb_refresh_2.setProperty("value", 60000)
        self.rb_refresh_2.setObjectName("rb_refresh_2")
        self.gridLayout_8.addWidget(self.rb_refresh_2, 0, 1, 1, 1)
        self.rb_refresh_3 = QtWidgets.QRadioButton(self.gb_refresh)
        self.rb_refresh_3.setProperty("value", 180000)
        self.rb_refresh_3.setObjectName("rb_refresh_3")
        self.gridLayout_8.addWidget(self.rb_refresh_3, 1, 0, 1, 1)
        self.rb_refresh_off = QtWidgets.QRadioButton(self.gb_refresh)
        self.rb_refresh_off.setProperty("value", 0)
        self.rb_refresh_off.setObjectName("rb_refresh_off")
        self.gridLayout_8.addWidget(self.rb_refresh_off, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.gb_refresh, 0, 3, 1, 1)
        self.pb_reload = QtWidgets.QPushButton(self.topwdg)
        self.pb_reload.setMinimumSize(QtCore.QSize(75, 70))
        self.pb_reload.setMaximumSize(QtCore.QSize(75, 66))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pb_reload.setFont(font)
        self.pb_reload.setStyleSheet("text-align:bottom;\n"
"padding-bottom:5px;\n"
"color: rgb(0, 65, 0);")
        self.pb_reload.setObjectName("pb_reload")
        self.gridLayout_5.addWidget(self.pb_reload, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.topwdg, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPush = QtWidgets.QAction(MainWindow)
        self.actionPush.setObjectName("actionPush")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "???"))
        self.pb_log_clear.setText(_translate("MainWindow", "????????????????"))
        self.pb_log_restore.setText(_translate("MainWindow", "??????????????"))
        self.la_header.setText(_translate("MainWindow", "?????????????????????????? ????????????????????????"))
        self.chb_oam.setText(_translate("MainWindow", "?????????? ???????????? ????????"))
        self.chb_bnp.setText(_translate("MainWindow", "proBNP"))
        self.chb_crd.setText(_translate("MainWindow", "??????????????????????????"))
        self.chb_xra.setText(_translate("MainWindow", "????????????????????????????"))
        self.chb_tni.setText(_translate("MainWindow", "???????????????? I hs"))
        self.la_instr.setText(_translate("MainWindow", "????????????????????????????????"))
        self.chb_abc.setText(_translate("MainWindow", "???????????????? SARS-CoV-2"))
        self.la_lab.setText(_translate("MainWindow", "????????????????????????"))
        self.chb_usd.setText(_translate("MainWindow", "??????"))
        self.chb_psp.setText(_translate("MainWindow", "??????????????????"))
        self.chb_cts.setText(_translate("MainWindow", "????"))
        self.chb_bak.setText(_translate("MainWindow", "?????????????????????????? ????????????"))
        self.chb_end.setText(_translate("MainWindow", "????????????????????"))
        self.chb_acb.setText(_translate("MainWindow", "??????"))
        self.chb_ddm.setText(_translate("MainWindow", "D-??????????"))
        self.chb_glu.setText(_translate("MainWindow", "?????????????? (??????????????.)"))
        self.chb_agc.setText(_translate("MainWindow", "Ag SARS-CoV-2"))
        self.chb_oak.setText(_translate("MainWindow", "?????????? ???????????? ??????????"))
        self.chb_dia.setText(_translate("MainWindow", "?????????????? ????????"))
        self.la_birthdate.setText(_translate("MainWindow", "26.01.1992"))
        self.la_name.setText(_translate("MainWindow", "?????????????? ?????? ????????????????"))
        self.gb_filter.setTitle(_translate("MainWindow", "???????????? ???? ??????????????????"))
        self.chb_filter_7.setText(_translate("MainWindow", "?????????????? 7"))
        self.chb_filter_9.setText(_translate("MainWindow", "?????????????? 9"))
        self.chb_filter_T.setText(_translate("MainWindow", "????????????????"))
        self.chb_filter_X.setText(_translate("MainWindow", "????????????"))
        self.gb_notifytype.setTitle(_translate("MainWindow", "?????????????????? ?????? ?????????????????? ??????????????"))
        self.rb_notifytype_off.setText(_translate("MainWindow", "??????????????????"))
        self.rb_notifytype_off.setProperty("property", _translate("MainWindow", "verbosity"))
        self.rb_notifytype_log.setText(_translate("MainWindow", "???????????? ?? ??????"))
        self.rb_notifytype_log.setProperty("property", _translate("MainWindow", "verbosity"))
        self.rb_notifytype_notification.setText(_translate("MainWindow", "??????????????????????"))
        self.rb_notifytype_notification.setProperty("property", _translate("MainWindow", "verbosity"))
        self.rb_notifytype_popup.setText(_translate("MainWindow", "?????????????????????? ????????"))
        self.rb_notifytype_popup.setProperty("property", _translate("MainWindow", "verbosity"))
        self.gb_refresh.setTitle(_translate("MainWindow", "????????????????????????????"))
        self.rb_refresh_05.setText(_translate("MainWindow", "30 ??????"))
        self.rb_refresh_05.setProperty("property", _translate("MainWindow", "autorefresh"))
        self.rb_refresh_2.setText(_translate("MainWindow", "1 ??????"))
        self.rb_refresh_2.setProperty("property", _translate("MainWindow", "autorefresh"))
        self.rb_refresh_3.setText(_translate("MainWindow", "3 ??????"))
        self.rb_refresh_3.setProperty("property", _translate("MainWindow", "autorefresh"))
        self.rb_refresh_off.setText(_translate("MainWindow", "????????"))
        self.rb_refresh_off.setProperty("property", _translate("MainWindow", "autorefresh"))
        self.pb_reload.setText(_translate("MainWindow", "????"))
        self.actionPush.setText(_translate("MainWindow", "Push-??????????????????????"))
from customobjects.QCheckBox import BuddyCheckBox
from customobjects.QGroupBox import GroupBoxWithRadiobuttons
from customobjects.QTableView import CustomTableView
