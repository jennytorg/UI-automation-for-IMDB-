from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


class coming_soon:

    header_new_movies = (By.CSS_SELECTOR, "h1[class='header'] a[class='newmovies']")
    tab_coming_soon = (By.CSS_SELECTOR, "#main div ul li.active a")

    first_movie_name = (By.XPATH, '//a[contains(@href,"?ref_=cs_ov_tt")]')
    add_to_watchlist = (By.CSS_SELECTOR, "a[class*='btn2_text_on'] span[class='btn2_text']")

    #'//a[@href="'+url+'"]'
    #“//tag [contains( text(), ‘word’)]”

    def __init__(self,driver):
        self.driver = driver

    def get_header_title_new_mov(self,driver):
        return driver.find_element(*coming_soon.header_new_movies)

    def get_title_coming_soon(self,driver):
        return driver.find_element(*coming_soon.tab_coming_soon)

    def get_first_movie_name(self,driver):
        return driver.find_element(*coming_soon.first_movie_name)

    def get_add_to_watchlist_btn(self,driver):
        return driver.find_element(*coming_soon.add_to_watchlist)




    def action_check_subtitles_page(self):
        
        time.sleep(2)
        title_text = self.get_header_title_new_mov(self.driver).text #text new movies
        assert title_text == 'New Movies'
        sub_text= self.get_title_coming_soon(self.driver).text #text: coming soon
        assert sub_text == 'Coming Soon'
        time.sleep(2)
        
    # grab the first movie name in the top, checks if the the button add to watchlist checked and if not, click on it 
    def action02_get_first_movie_name_click_watchlist(self):
        
        time.sleep(2)
        mvname = self.get_first_movie_name(self.driver).text
        print(mvname)
        self.driver.execute_script("window.scrollTo(0,500)")

        #(note) click on first button 'add to watch list' if it not clicked
        button= self.get_add_to_watchlist_btn(self.driver)
        if button.text == 'Add to Watchlist':
            button.click()
        elif button.text == 'Watchlist':
            print('the first movie is already in your watch list')

    
        time.sleep(2)
        return mvname