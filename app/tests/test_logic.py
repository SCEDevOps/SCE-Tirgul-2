
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

################# Get In with correct details #################
chromedriver = "/Users/LITALHO/PycharmProjects/SCE-Tirgul-2/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('http://127.0.0.1:5000/')
first_name_Input = browser.find_element_by_id("first_name")
first_name_Input.send_keys("lilo")
last_name_Input = browser.find_element_by_id("last_name")
last_name_Input.send_keys("siksik")
id_Input =  browser.find_element_by_id("user_id")
id_Input.send_keys("66")
id_Input.send_keys(Keys.ENTER)
browser.close()
#################################################################