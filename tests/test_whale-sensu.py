import unittest

from sensu_plugin import SensuHandler

from whale_sensu.handler import WhaleHandler


class TestWhaleSensu(unittest.TestCase):

    def setUp(self):
        pass

    def test_return_value(self):
        handler = WhaleHandler()
        self.assertTrue(handler, SensuHandler)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
