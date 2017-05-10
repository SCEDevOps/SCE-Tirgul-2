import unittest
from app import app

class WebTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.check = self.app.test_client(self)
        self.check.testing = True

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

if __name__ == '__main__':
    unittest.main()