# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/talkeditor_about.ui'
#
# Created: Tue Apr  5 00:59:10 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_TalkEditorAbout(object):
    def setupUi(self, TalkEditorAbout):
        TalkEditorAbout.setObjectName("TalkEditorAbout")
        TalkEditorAbout.resize(516, 410)
        self.gridLayout_2 = QtGui.QGridLayout(TalkEditorAbout)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(TalkEditorAbout)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/freeseer/freeseer_logo.png"))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.aboutInfo = QtGui.QLabel(TalkEditorAbout)
        self.aboutInfo.setTextFormat(QtCore.Qt.RichText)
        self.aboutInfo.setWordWrap(True)
        self.aboutInfo.setOpenExternalLinks(True)
        self.aboutInfo.setObjectName("aboutInfo")
        self.gridLayout_2.addWidget(self.aboutInfo, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TalkEditorAbout)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(TalkEditorAbout)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TalkEditorAbout.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TalkEditorAbout.reject)
        QtCore.QMetaObject.connectSlotsByName(TalkEditorAbout)

    def retranslateUi(self, TalkEditorAbout):
        TalkEditorAbout.setWindowTitle(QtGui.QApplication.translate("TalkEditorAbout", "About Talk Database Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutInfo.setText(QtGui.QApplication.translate("TalkEditorAbout", "Freeseer", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
