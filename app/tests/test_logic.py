from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from app import db, app
from app.models import User

class Test_Selenium(LiveServerTestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(app)
        with app.app_context():
            db.create_all()
            db.session.commit()
            lilo = User('lilo', 'siksik', 66)
            db.session.add(lilo)
            db.session.commit()
        return app

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.get(self.browser.get(self.get_server_url()))
        self.time = time
        self.str ='המצביע אינו מופיע בבסיס הנתונים או שכבר הצביע'
        # db.drop_all()
        # db.create_all()
        # db.session.commit()
        # lilo = User('lilo', 'siksik', 66)
        # db.session.add(lilo)
        # db.session.commit()

    def test_correct_details(self):
        ################# Get In with correct details #################
        browser =  self.browser
        first_name_Input = browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = browser.find_element_by_id("last_name")
        last_name_Input.send_keys("siksik")
        id_Input = browser.find_element_by_id("user_id")
        id_Input.send_keys("66")
        id_Input.send_keys(Keys.ENTER)
        #self.time.sleep(5)
        assert self.str not in self.browser.page_source

        #browser.save_screenshot('correctDatails.png')

    def test_incorrect_details(self):
        ################# Try to Get In with incorrect details ##########
        browser =  self.browser
        first_name_Input = browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = browser.find_element_by_id("last_name")
        last_name_Input.send_keys("horesh")
        id_Input = browser.find_element_by_id("user_id")
        id_Input.send_keys("222")
        id_Input.send_keys(Keys.ENTER)
        #self.time.sleep(5)
        assert self.str in self.browser.page_source
        #browser.save_screenshot('incorrectDatails.png')
        #################################################################

    def tearDown(self):
        self.browser.close()
        with app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()