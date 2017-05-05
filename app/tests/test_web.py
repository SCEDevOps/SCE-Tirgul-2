import os
import unittest
from app import app, db
from app.models import User, Party
from flask_config import basedir

class AppTestCase(unittest.TestCase):

    basedir = os.path.abspath(os.path.dirname(__file__))

    def setUp(self):
        self.app = app
        self.tester = self.app.test_client(self)
        self.tester.testing = True

######## The manager page is not Unaccessible from the url ########
    def test_Manager_Option(self):
        response = self.tester.get('/app/manager')
        self.assertEqual(response.status_code, 404) #404=not founf
###################################################################

if __name__ == '__main__':
    unittest.main()