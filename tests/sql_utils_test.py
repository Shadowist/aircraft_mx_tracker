""" Unit tests for the sql_utils module. """
# Standard Library
import unittest
from pathlib import Path
from source.sql_manager import sql_manager

TAIL_NUMBER = "N1234"


class SqlUtilsTestCase(unittest.TestCase):
    """ Main test case class. """
    path = Path()

    def setUp(self):
        self.path = Path(TAIL_NUMBER)

    def tearDown(self):
        self.path.unlink()

    def test_create_connection(self):
        """ Test creating a new connection. """
        sql_manager.open_file(str(self.path))

        self.assertTrue(self.path.exists())
