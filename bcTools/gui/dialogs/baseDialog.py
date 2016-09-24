"""
"""
from PyQt4 import QtCore
from PyQt4 import QtGui

from bcTools.gui.resources import Ui_BaseDialog
from bcTools.gui.resources import designer_rc


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
	css = QtCore.QFile(':/root/resources/stylesheets/DarkOrange/style.qss')
	print css.exists()
	css.open(QtCore.QIODevice.ReadOnly)
	stylesheet = ""
	if css.isOpen():
		# ts = QTextStream(f)
		# stylesheet = ts.readAll()
		stylesheet = QtCore.QVariant(css.readAll()).toString()
	css.close()
	print stylesheet
	application = QtGui.QApplication([])
	dialog = BaseDialog()
	dialog.setStyleSheet(stylesheet)
	dialog.show()
	application.exec_()


if __name__ == '__main__':
	main()
