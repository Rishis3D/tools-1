""" Test module for bcTools.utilities.sequenceLister
"""
import argparse

from bcTesting import testBase
from bcTools.cli import sequenceLister


class Test_SequenceLister(testBase.TestCase):
	""" Test class for all the module level functions of
		bcTools.utilities.sequenceLister.
	"""
	def test_getArguments_success(self):
		""" Basic test for module level function _getArguments
		"""
		self.assertType(sequenceLister._getParser([]), argparse.Namespace)

	def test_sequenceLister(self):
		""" Basic test for module level function _getArguments
		"""
		self.monkeyPatch("sys.argv", ["sequenceLister"])
		self.assertFalse(sequenceLister.sequenceLister())
