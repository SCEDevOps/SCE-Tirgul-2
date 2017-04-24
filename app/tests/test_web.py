from app.views import login, validateUser
import unittest
import nose
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('flask_config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views, models


class name(unittest.TestCase):

    def test_p(self):
        self.assertFalse(validateUser("rom","siksik","22"))
        #testttgsdf


if __name__ == '__main__':
    unittest.main()
