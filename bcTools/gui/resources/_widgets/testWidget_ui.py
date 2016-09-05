# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/cygdrive/w/developments/GitHub/tools/resources/pyqt/widgets/testWidget.ui'
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

class Ui_TestWidget(object):
    def setupUi(self, TestWidget):
        TestWidget.setObjectName(_fromUtf8("TestWidget"))
        TestWidget.resize(568, 181)

        self.retranslateUi(TestWidget)
        QtCore.QMetaObject.connectSlotsByName(TestWidget)

    def retranslateUi(self, TestWidget):
        TestWidget.setWindowTitle(_translate("TestWidget", "Form", None))

