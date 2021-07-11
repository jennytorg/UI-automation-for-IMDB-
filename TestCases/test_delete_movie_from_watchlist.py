from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

from pageObjects_web.header import header_links__imdb
from pageObjects_web.loginPage import login
from pageObjects_web.your_watch_list_page import watch_list
from pageObjects_web.edit_your_watch_list import edit_watchList_imdb


from .Get_data_func import get_data_method


class Test_watchList_edit:

    pytest.movies_list_befor =[]
    
    @classmethod
    def setup_class(cls):
        global driver
        global header_btn
        global login_process
        global get_data_xml
        global coming_soon_list
        global watch_list_page
        global edit_my_list

        driver = webdriver.Chrome(ChromeDriverManager().install())
        get_data_xml = get_data_method()
        url = get_data_xml.get_data("url")
        time.sleep(3)
        driver.get(url)
        # print(url)
        # time.sleep(1)
        driver.maximize_window()
        ##driver.get("https://www.imdb.com/")
        driver.implicitly_wait(10)
        header_btn = header_links__imdb(driver)
        login_process  = login(driver)
        watch_list_page=watch_list(driver)
        edit_my_list = edit_watchList_imdb(driver)

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def test_sing_in_imdb(self):
        try:
            header_btn.get_sign_in(driver).click()
            login_process.action_click_imdb_signin()
            
            usr_email = get_data_xml.get_data("user")
            passwrd = get_data_xml.get_data("password")
            login_process.action_fill_the_form_signin(usr_email, passwrd)

        except Exception as e:
            print(e)
            pytest.fail(str(e))

#click the watchlist in the header after signin
    def test_click_on_watch_list_after_signin(self):
        try:
            header_btn.action04_click_on_watchlist()
            watch_list_page.action_verify_watch_list_page_loaded()

        except Exception as e:
            print(e)
            pytest.fail(str(e))

# after the user watchlist loaded , clicks on edit button and verify the edit format loaded 
    def test_click_edit_and_verify(self):
        try:
            watch_list_page.action03_click_on_edit_button()
            edit_my_list.action_verify_edit_page()
            
        except Exception as e:
            print(e)
            pytest.fail(str(e))


# class list - find all  movie names in the list and return it to test class    
    def test_save_all_movie_names_before_delete(self):
        try:
            ##save in arr movie list before 
            pytest.movies_list_befor = edit_my_list.action03_get_all_movie_names_in_the_list()
            
        except Exception as e:
            print(e)
            pytest.fail(str(e))


# verify the delete button disabled and all checkboxes are unchecked, and then check the LAST checkbox from 3 
    def test_verify_delete_btn_disbld_and_check_last_box(self):
        try:
            edit_my_list.action02_check_the_last_checkbox()
            
        except Exception as e:
            print(e)
            pytest.fail(str(e))

# after the checkbox on - verify the delete link enabled and click on it, comfirm popapp to delete the last movie from the list
    def test_verify_delete_btn_enabled_and_delete_movie(self):
        try:
            edit_my_list.action04_click_on_delete_movie()

        except Exception as e:
            print(e)
            pytest.fail(str(e))


#get movie list after and compare to before delete (general compare by len lists)
    def test_check_the_movie_list_before_and_after(self):
        try:
            movie_list_after=[]
            movie_list_after = edit_my_list.action03_get_all_movie_names_in_the_list()
            
            assert not len(pytest.movies_list_befor) == len(movie_list_after)

        except Exception as e:
            print(e)
            pytest.fail(str(e))