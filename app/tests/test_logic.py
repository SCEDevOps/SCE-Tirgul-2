from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from app import db
from app.models import User

class SeleniumTest(unittest.TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        print('done creatin app ')
        return app

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get("http://localhost:8943")


        # self.browser = webdriver.PhantomJS()
        # self.time = time
        # self.str ='המצביע אינו מופיע בבסיס הנתונים או שכבר הצביע'
        # db.drop_all()
        # db.create_all()
        # db.session.commit()
        # lilo = User('lilo', 'siksik', 66)
        # db.session.add(lilo)
        # db.session.commit()

    def test_correct_details(self):
        ################# Get In with correct details #################
        browser =  self.browser
        browser.get('http://127.0.0.1:5000/')
        first_name_Input = browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = browser.find_element_by_id("last_name")
        last_name_Input.send_keys("siksik")
        id_Input = browser.find_element_by_id("user_id")
        id_Input.send_keys("66")
        id_Input.send_keys(Keys.ENTER)
        self.time.sleep(5)
        assert self.str not in self.browser.page_source

        #browser.save_screenshot('correctDatails.png')

    def test_incorrect_details(self):
        ################# Try to Get In with incorrect details ##########
        browser =  self.browser
        browser.get('http://127.0.0.1:5000/')
        first_name_Input = browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = browser.find_element_by_id("last_name")
        last_name_Input.send_keys("horesh")
        id_Input = browser.find_element_by_id("user_id")
        id_Input.send_keys("222")
        id_Input.send_keys(Keys.ENTER)
        self.time.sleep(5)
        assert self.str in self.browser.page_source
        #browser.save_screenshot('incorrectDatails.png')
        #################################################################

    def test_home(self):
        assert "Flask Intro - login page" == self.driver.title
        #

    def tearDown(self):
        self.browser.close()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()