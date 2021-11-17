import connex_app
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        connex_app.app.testing = True
        self.app = connex_app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        # Make your assertions