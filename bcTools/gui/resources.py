""" Public interface for bcTools.gui.resources
"""
from bcTools.gui._resources._dialogs.baseDialog_ui import Ui_BaseDialog
from bcTools.gui._resources._widgets.testWidget_ui import Ui_TestWidget
from bcTools.gui._resources import designer_rc as pyqtResouces
from bcTools.gui._resources import styleSheets

__all__ = [
	"Ui_BaseDialog",
	"Ui_TestWidget",
	"styleSheets",
	"pyqtResouces"
]
