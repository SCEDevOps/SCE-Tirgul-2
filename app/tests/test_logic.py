import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask
from flask_testing import LiveServerTestCase
from app.models import User, Party
from app import app , db


class SeleniumTest(LiveServerTestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        db.init_app(app)
        with app.app_context():
            db.create_all()
            self.insert_data_to_db()
        return app

    def insert_data_to_db(self):
        db.session.commit()
        admon = User('tomer', 'admon', '123')
        avoda = Party(u'׳”׳¢׳‘׳•׳“׳”',
                      'https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg')
        db.session.add(avoda)
        db.session.add(admon)
        db.session.commit()

    def setUp(self):
        # create a new Firefox session
         self.browser = webdriver.PhantomJS()
         # nevigate to the application home page
         self.browser.get(self.get_server_url())

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
        first_name_Input = self.browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = self.browser.find_element_by_id("last_name")
        last_name_Input.send_keys("siksik")
        id_Input = self.browser.find_element_by_id("user_id")
        id_Input.send_keys("66")
        id_Input.send_keys(Keys.ENTER)
        assert self.str not in self.browser.page_source

        #browser.save_screenshot('correctDatails.png')

    def test_incorrect_details(self):
        ################# Try to Get In with incorrect details ##########
        first_name_Input = self.browser.find_element_by_id("first_name")
        first_name_Input.send_keys("lilo")
        last_name_Input = self.browser.find_element_by_id("last_name")
        last_name_Input.send_keys("horesh")
        id_Input = self.browser.find_element_by_id("user_id")
        id_Input.send_keys("222")
        id_Input.send_keys(Keys.ENTER)
        assert self.str in self.browser.page_source
        #browser.save_screenshot('incorrectDatails.png')
        #################################################################

    def test_home(self):
        assert "Flask Intro - login page" == self.browser.title
        ###

    def tearDown(self):
        self.browser.quit()
        with app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == '__main__':
    unittest.main()