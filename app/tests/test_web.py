import unittest
from app import app
from app import db

class WebTest(unittest.TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        self.check = app.test_client(self)

######## The manager page is not Unaccessible from the url ########
    def test_Manager_Option(self):
        response = self.check.get('/app/manager')
        self.assertEqual(response.status_code, 404) #404=not founf
###################################################################

##################### Cant log in without id ######################
    def test_missing_id_(self):
        response = self.check.post('login',data=dict(first_name='lilo', last_name='siksik'))
        self.assertEqual(response.status_code, 400) # 400=Bad Request
###################################################################

#################### not in db - err message ######################
    def test_error_message(self):
        response = self.check.post('login',data=dict(first_name='dummy', last_name='dummy',user_id ='1'))
        str = response.data.decode('utf-8')
        assert 'המצביע אינו מופיע בבסיס הנתונים או שכבר הצביע' in str
###################################################################

    def tearDown(self):
        del self.check
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


if __name__ == '__main__':
    unittest.main()