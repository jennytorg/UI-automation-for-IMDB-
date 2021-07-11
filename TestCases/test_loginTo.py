from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

from pageObjects_web.header import header_links__imdb
from pageObjects_web.loginPage import login


from selenium.webdriver.common.keys import Keys
from .Get_data_func import get_data_method


class Test_imdb_login:
    
    @classmethod
    def setup_class(cls):
        global driver
        global header_btn
        global login_process
        global get_data_xml
        driver = webdriver.Chrome(ChromeDriverManager().install())
        get_data_xml = get_data_method()
        url = get_data_xml.get_data("url")
        time.sleep(3)
        driver.get(url)
        print(url)
        time.sleep(1)
        driver.maximize_window()
        ##driver.get("https://www.imdb.com/")
        driver.implicitly_wait(10)
        header_btn = header_links__imdb(driver)
        login_process  = login(driver)
    
    @classmethod
    def teardown_class(cls):
        driver.quit()
         

    def test_click_on_sign_in(self):
        try:
            
            header_btn.get_sign_in(driver).click()

            
        except Exception as e:
            print(e)
            pytest.fail(str(e))

    def test_sign_in_list(self):
        try:
            login_process.action_click_imdb_signin()
            
                
        except Exception as e:
            print(e)
            pytest.fail(str(e))


    def test_sign_in_account(self):
        try:
            usr_email = get_data_xml.get_data("user")
            passwrd = get_data_xml.get_data("password")
            login_process.action_fill_the_form_signin(usr_email, passwrd)            
                
        except Exception as e:
            print(e)
            pytest.fail(str(e))

##to verify that after the click the user logedin to his account and back to the main page
    def test_verify_redirct_hp(self):
        try:
            header_btn.action01_verify_user_hp()
                
        except Exception as e:
            print(e)
            pytest.fail(str(e))


    def test_verify_logged_in02(self):
        try:
            header_btn.action02_verify_user_logedin()
            
                
        except Exception as e:
            print(e)
            pytest.fail("test fail, see error ",str(e))