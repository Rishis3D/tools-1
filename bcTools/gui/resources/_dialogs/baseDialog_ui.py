# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/cygdrive/w/developments/GitHub/tools/resources/pyqt/dialogs/baseDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BaseDialog(object):
    def setupUi(self, BaseDialog):
        BaseDialog.setObjectName(_fromUtf8("BaseDialog"))
        BaseDialog.resize(566, 195)
        self.verticalLayout = QtGui.QVBoxLayout(BaseDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainVLayout = QtGui.QVBoxLayout()
        self.mainVLayout.setSpacing(3)
        self.mainVLayout.setObjectName(_fromUtf8("mainVLayout"))
        self.bannerHLayout = QtGui.QHBoxLayout()
        self.bannerHLayout.setObjectName(_fromUtf8("bannerHLayout"))
        self.mainVLayout.addLayout(self.bannerHLayout)
        self.contentVLayout = QtGui.QVBoxLayout()
        self.contentVLayout.setObjectName(_fromUtf8("contentVLayout"))
        self.mainVLayout.addLayout(self.contentVLayout)
        self.mainVLayout.setStretch(1, 100)
        self.verticalLayout.addLayout(self.mainVLayout)

        self.retranslateUi(BaseDialog)
        QtCore.QMetaObject.connectSlotsByName(BaseDialog)

    def retranslateUi(self, BaseDialog):
        BaseDialog.setWindowTitle(_translate("BaseDialog", "Dialog", None))

