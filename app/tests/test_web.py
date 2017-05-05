from app.views import login, validateUser
import unittest
import nose
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



from app import views, models, app


class name(unittest.TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object('flask_config')
        db = SQLAlchemy(app)
        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = 'login'

    def test_p(self):
        self.assertFalse(validateUser("rom","siksik","22"))
        #testttgsdf

    def test_d(self):
        self.app =app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #TEST ADDED

    # def test_loginn(self):
    #     with app.app_context():
    #         res= self.app.login('/login', data=dict(
    #             first_name="rom",
    #             last_name="siksik",
    #             user_id="33"
    #             ), follow_redirects=True)
    #     assert b'You were logged in' in res.data


    # def test_invaild_login(self):
    #     self.app = app.test_client()
    #     invalid_login = app.post('login', data=dict(login='invalid', password='invalid'), follow_redirects=True)
    #     assert 'Invalid credentials' in invalid_login.data


if __name__ == '__main__':
    unittest.main()
def trying():
    trying=1