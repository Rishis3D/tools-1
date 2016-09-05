"""
"""
from PyQt4 import QtGui

from bcTools.gui.resources import Ui_BaseDialog


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
		self._ui.setUp(self)

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

