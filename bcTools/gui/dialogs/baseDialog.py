""" Base PyQt Dialog for all GUI tools inside the project
"""
from PyQt4 import QtCore
from PyQt4 import QtGui

from bcTools.gui.resources import Ui_BaseDialog
from bcTools.gui.resources import styleSheets


class BaseDialog(QtGui.QDialog):
	"""
	"""
	def __init__(self, parent=None):
		super(BaseDialog, self).__init__(parent)

		self._ui = Ui_BaseDialog()
		self._setUp()

	def _setUp(self):
		"""
		"""
		self._ui.setupUi(self)

	def setBannerImage(self, image):
		"""
		"""
		pass

	def addWidget(self, widget):
		"""
		"""
		self._ui.contentVLayout.addWidget(widget)

	def addLayout(self, layout):
		"""
		"""
		self._ui.contentVLayout.addLayout(layout)


def main():
	application = QtGui.QApplication([])
	dialog = BaseDialog()
	dialog.setStyleSheet(styleSheets.getStyleSheet("DarkOrange"))
	dialog.show()
	application.exec_()


if __name__ == '__main__':
	main()
