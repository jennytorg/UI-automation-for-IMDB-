from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

from pageObjects_web.header import header_links__imdb
from pageObjects_web.loginPage import login
from pageObjects_web.new_mov_coming_soon import coming_soon_imdb
from pageObjects_web.your_watch_list_page import watch_list


from .Get_data_func import get_data_method


class Test_watchList_select_and_add:

    pytest.movie_title = None
    
    @classmethod
    def setup_class(cls):
        global driver
        global header_btn
        global login_process
        global get_data_xml
        global coming_soon_list
        global watch_list_page
        
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
        coming_soon_list = coming_soon_imdb(driver)
        watch_list_page=watch_list(driver)
        
    
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


    def test_from_menu_select_coming_soon(self):
        try:
            header_btn.action03_click_on_menu_and_select_coming_soon()
            
        except Exception as e:
            print(e)
            pytest.fail(str(e))


    def test_coming_soon_page_load(self):
        try:
            coming_soon_list.action_check_subtitles_page()

        except Exception as e:
            print(e)
            pytest.fail(str(e))

# from coming soon list of movies, clicks on the first 'add to watchlist' button from the top
    def test_select_movie_add_to_watch_list(self):
        try:
            pytest.movie_title = coming_soon_list.action02_get_first_movie_name_click_watchlist()

        except Exception as e:
            print(e)
            pytest.fail(str(e))

    def test_verify_movie_added_and_print_all_names(self):
        try:

            header_btn.action04_click_on_watchlist()

            watch_list_page.action_verify_watch_list_page_loaded()
            watch_list_page.action02_find_movie_list_and_check_the_mov_added(pytest.movie_title)

        except Exception as e:
            print(e)
            pytest.fail(str(e))

