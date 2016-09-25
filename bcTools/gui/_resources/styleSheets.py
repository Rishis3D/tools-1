""" Module contains helper function for PyQt4 stylesheets.
"""
from PyQt4 import QtCore

from bcTools import exceptions as _exceptions
from bcTools.gui import common as _guiCommon
from bcTools.gui._resources import designer_rc


def availableStyleSheets():
	""" Helper function to get all style sheets available in the resources

	Returns:
		(QStringList): List of stylesheet names as QString.
	"""
	styleSheets = QtCore.QStringList()
	styleSheetsDirectory = QtCore.QDir(_guiCommon.styleSheetRootDirectory)
	if styleSheetsDirectory.exists():
		print "something here"
		styleSheetsDirectory.setFilter(QtCore.QDir.Dirs)
		for styleSheet in styleSheetsDirectory.entryList():
			styleSheets.append(styleSheet)
	styleSheets.sort()
	return styleSheets


def getStyleSheet(name=None):
	""" Helper function to get the style sheet for the given name

	Args:
		name (str): Name of the stylesheet

	Raises:
		(ResourceNotFound): Raises if the style sheet is not available.

	Returns:
		(QString): Content of stylesheet files inside the directory.
	"""
	name = QtCore.QString(name or _guiCommon.defaultStyleSheet)

	if name not in availableStyleSheets():
		raise _exceptions.ResourceNotFound(
			"The given stylesheet(%s) is not available in resources." % name
		)

	styleSheetDirectory = QtCore.QDir(
		QtCore.QDir(_guiCommon.styleSheetRootDirectory).filePath(name)
	)

	styleSheet = QtCore.QString()
	for fileInfo in styleSheetDirectory.entryInfoList():
		qssFilePath = fileInfo.absoluteFilePath()
		for fileType in _guiCommon.styleSheetsFileTypes:
			if qssFilePath.endsWith(fileType):
				qssFile = QtCore.QFile(qssFilePath)
				qssFile.open(QtCore.QIODevice.ReadOnly)
				if qssFile.isOpen():
					styleSheet.append(
						QtCore.QVariant(qssFile.readAll()).toString()
					)
	return styleSheet
