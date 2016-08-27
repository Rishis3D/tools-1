""" Module contains the base class for the testing of core python modules/functions.
"""
import mox
import testtools


class TestCase(testtools.TestCase):
    """ Base class for bcTesting project.
    """

    def setUp(self):
        """
        """
        super(TestCase, self).setUp()
        self._mox = mox.Mox()

    def tearDown(self):
        """
        """
        super(TestCase, self).tearDown()
        self._mox.UnsetStubs()
