from selenium.webdriver.common.by import By
import time

class header_links__imdb:
   
    menu = (By.ID,"imdbHeader-navDrawerOpen--desktop")
    watch_list = (By.XPATH, "//*[@id='imdbHeader']/div[2]/div[4]/a")
    sign_in = (By.XPATH, "//*[@id='imdbHeader']/div[2]/div[5]/a/div")
    home = (By.ID,"home_img_holder")
    account_name = (By.CSS_SELECTOR, "div[class ='ipc-button__text' ]  span[class*='account-toggle']")
    menu_coming_soon = (By.XPATH, '//a[@href="https://www.imdb.com/coming-soon/?ref_=nv_mv_cs"]')

    def __init__(self,driver):
        self.driver = driver


    def get_menu(self,driver):
        return driver.find_element(*header_links__imdb.menu)

    def get_watch_list(self,driver):
        return driver.find_element(*header_links__imdb.watch_list)

    def get_sign_in(self,driver):
        return driver.find_element(*header_links__imdb.sign_in)

    def get_home_page_icon(self,driver):
        return driver.find_element(*header_links__imdb.home)

    def get_user_name_header(self,driver):
        return driver.find_element(*header_links__imdb.account_name)

    def get_coming_soon(self,driver):
        return driver.find_element(*header_links__imdb.menu_coming_soon)



    def action01_verify_user_hp(self):
        time.sleep(2)
        hpTitle = self.driver.title 
        #back to the homepage 
        print(hpTitle)
        
        assert hpTitle == 'IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows'
        

    def action02_verify_user_logedin(self):
       
        #instead of the sign in , now the 'user name' display 
        usrac = self.get_user_name_header(self.driver).text
        time.sleep(2)
        assert usrac == 'Jennyt'
        time.sleep(2)
    
    def action03_click_on_menu_and_select_coming_soon(self):
        
        self.get_menu(self.driver).click()
        time.sleep(2)
        self.get_coming_soon(self.driver).click()
        

    def action04_click_on_watchlist(self):
        
        self.get_watch_list(self.driver).click()
        time.sleep(2)