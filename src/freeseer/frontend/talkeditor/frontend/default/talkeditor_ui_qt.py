# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/talkeditor_ui_qt.ui'
#
# Created: Tue Apr  5 00:59:10 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TalkEditorMainWindow(object):
    def setupUi(self, TalkEditorMainWindow):
        TalkEditorMainWindow.setObjectName("TalkEditorMainWindow")
        TalkEditorMainWindow.resize(884, 497)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/freeseer/freeseer_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TalkEditorMainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(TalkEditorMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addTalkGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.addTalkGroupBox.setObjectName("addTalkGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.addTalkGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(self.addTalkGroupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.roomEdit = QtGui.QLineEdit(self.addTalkGroupBox)
        self.roomEdit.setEnabled(False)
        self.roomEdit.setInputMask("")
        self.roomEdit.setObjectName("roomEdit")
        self.gridLayout_2.addWidget(self.roomEdit, 2, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.addTalkGroupBox)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 2, 2, 1, 1)
        self.titleEdit = QtGui.QLineEdit(self.addTalkGroupBox)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout_2.addWidget(self.titleEdit, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.addTalkGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.addTalkGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.presenterEdit = QtGui.QLineEdit(self.addTalkGroupBox)
        self.presenterEdit.setEnabled(False)
        self.presenterEdit.setInputMask("")
        self.presenterEdit.setObjectName("presenterEdit")
        self.gridLayout_2.addWidget(self.presenterEdit, 4, 1, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.addTalkGroupBox)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 4, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.addTalkGroupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.eventEdit = QtGui.QLineEdit(self.addTalkGroupBox)
        self.eventEdit.setEnabled(False)
        self.eventEdit.setObjectName("eventEdit")
        self.gridLayout_2.addWidget(self.eventEdit, 1, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.addTalkGroupBox)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.addTalkGroupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.addTalkGroupBox)
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 3, 1, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.addTalkGroupBox)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 3, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.confirmAddTalkButton = QtGui.QPushButton(self.addTalkGroupBox)
        self.confirmAddTalkButton.setObjectName("confirmAddTalkButton")
        self.horizontalLayout_9.addWidget(self.confirmAddTalkButton)
        self.cancelAddTalkButton = QtGui.QPushButton(self.addTalkGroupBox)
        self.cancelAddTalkButton.setObjectName("cancelAddTalkButton")
        self.horizontalLayout_9.addWidget(self.cancelAddTalkButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addWidget(self.addTalkGroupBox)
        self.talkEditorGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.talkEditorGroupBox.setObjectName("talkEditorGroupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.talkEditorGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtGui.QLabel(self.talkEditorGroupBox)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.rssEdit = QtGui.QLineEdit(self.talkEditorGroupBox)
        self.rssEdit.setObjectName("rssEdit")
        self.horizontalLayout_8.addWidget(self.rssEdit)
        self.rssButton = QtGui.QPushButton(self.talkEditorGroupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/rss_logo/rss_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rssButton.setIcon(icon1)
        self.rssButton.setObjectName("rssButton")
        self.horizontalLayout_8.addWidget(self.rssButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editTable = QtGui.QTableWidget(self.talkEditorGroupBox)
        self.editTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.editTable.setFrameShadow(QtGui.QFrame.Plain)
        self.editTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.editTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.editTable.setShowGrid(False)
        self.editTable.setWordWrap(False)
        self.editTable.setCornerButtonEnabled(False)
        self.editTable.setRowCount(0)
        self.editTable.setColumnCount(6)
        self.editTable.setObjectName("editTable")
        self.editTable.setColumnCount(6)
        self.editTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.editTable.setHorizontalHeaderItem(0, item)
        self.editTable.horizontalHeaderItem(0).setText("Speaker")
        item = QtGui.QTableWidgetItem()
        self.editTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.editTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.editTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.editTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.editTable.setHorizontalHeaderItem(5, item)
        self.editTable.horizontalHeaderItem(5).setText("Id")
        self.editTable.horizontalHeader().setCascadingSectionResizes(True)
        self.editTable.horizontalHeader().setDefaultSectionSize(142)
        self.editTable.horizontalHeader().setStretchLastSection(True)
        self.editTable.verticalHeader().setVisible(False)
        self.editTable.verticalHeader().setCascadingSectionResizes(True)
        self.editTable.verticalHeader().setSortIndicatorShown(True)
        self.editTable.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.editTable)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.addTalkButton = QtGui.QPushButton(self.talkEditorGroupBox)
        self.addTalkButton.setCheckable(True)
        self.addTalkButton.setObjectName("addTalkButton")
        self.verticalLayout_4.addWidget(self.addTalkButton)
        self.removeTalkButton = QtGui.QPushButton(self.talkEditorGroupBox)
        self.removeTalkButton.setObjectName("removeTalkButton")
        self.verticalLayout_4.addWidget(self.removeTalkButton)
        self.resetButton = QtGui.QPushButton(self.talkEditorGroupBox)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout_4.addWidget(self.resetButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.talkEditorGroupBox)
        TalkEditorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TalkEditorMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuLanguage = QtGui.QMenu(self.menuOptions)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        TalkEditorMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TalkEditorMainWindow)
        self.statusbar.setObjectName("statusbar")
        TalkEditorMainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(TalkEditorMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(TalkEditorMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.menuLanguage.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.roomEdit)
        self.label_3.setBuddy(self.titleEdit)
        self.label_4.setBuddy(self.presenterEdit)
        self.label_7.setBuddy(self.eventEdit)
        self.label_8.setBuddy(self.dateTimeEdit)
        self.label_9.setBuddy(self.rssEdit)

        self.retranslateUi(TalkEditorMainWindow)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.eventEdit.setEnabled)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL("toggled(bool)"), self.roomEdit.setEnabled)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL("toggled(bool)"), self.presenterEdit.setEnabled)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL("toggled(bool)"), self.dateTimeEdit.setEnabled)
        QtCore.QObject.connect(self.addTalkButton, QtCore.SIGNAL("toggled(bool)"), self.talkEditorGroupBox.setHidden)
        QtCore.QObject.connect(self.confirmAddTalkButton, QtCore.SIGNAL("clicked()"), self.addTalkButton.toggle)
        QtCore.QObject.connect(self.addTalkButton, QtCore.SIGNAL("toggled(bool)"), self.addTalkGroupBox.setVisible)
        QtCore.QObject.connect(self.cancelAddTalkButton, QtCore.SIGNAL("clicked()"), self.addTalkButton.toggle)
        QtCore.QMetaObject.connectSlotsByName(TalkEditorMainWindow)

    def retranslateUi(self, TalkEditorMainWindow):
        TalkEditorMainWindow.setWindowTitle(QtGui.QApplication.translate("TalkEditorMainWindow", "talk database editor", None, QtGui.QApplication.UnicodeUTF8))
        self.addTalkGroupBox.setTitle(QtGui.QApplication.translate("TalkEditorMainWindow", "Add Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Room", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Presenter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Event", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Date&Time", None, QtGui.QApplication.UnicodeUTF8))
        self.dateTimeEdit.setDisplayFormat(QtGui.QApplication.translate("TalkEditorMainWindow", "MM/dd/yyyy hh:mm ", None, QtGui.QApplication.UnicodeUTF8))
        self.confirmAddTalkButton.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelAddTalkButton.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.talkEditorGroupBox.setTitle(QtGui.QApplication.translate("TalkEditorMainWindow", "Talks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.rssButton.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Load talks from rss", None, QtGui.QApplication.UnicodeUTF8))
        self.editTable.setSortingEnabled(False)
        self.editTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.editTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Room", None, QtGui.QApplication.UnicodeUTF8))
        self.editTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Event", None, QtGui.QApplication.UnicodeUTF8))
        self.editTable.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("TalkEditorMainWindow", "DateTime", None, QtGui.QApplication.UnicodeUTF8))
        self.addTalkButton.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeTalkButton.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("TalkEditorMainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("TalkEditorMainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLanguage.setTitle(QtGui.QApplication.translate("TalkEditorMainWindow", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("TalkEditorMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("TalkEditorMainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("TalkEditorMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
import resource_rc
