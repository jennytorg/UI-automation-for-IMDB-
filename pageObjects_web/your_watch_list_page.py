from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


class watch_list:


    watch_list_title = (By.CSS_SELECTOR, "div.lister-header div div.nav-left h1")
    movie_titles = (By.CSS_SELECTOR,"h3.lister-item-header a")
    edit_button = (By.XPATH, '//a[@href="/list/ls505505706/edit?ref_=wl_edt_pwr"]')
    sort_by_DD = (By.ID, "lister-sort-by-options")

    #'//a[@href="'+url+'"]'
    #“//tag [contains( text(), ‘word’)]”

    def __init__(self,driver):
        self.driver = driver

    def get_page_subtitle(self,driver):
        return driver.find_element(*watch_list.watch_list_title)

    #(note) find all movies names in the list - arr
    def get_movie_titles(self,driver):
        return driver.find_elements(*watch_list.movie_titles)

    def get_edit_button(self,driver):
        return driver.find_element(*watch_list.edit_button)


    def get_sort_by_dropdown(self,driver):
        return driver.find_element(*watch_list.sort_by_DD)



# verify that the user watch list page loded 
    def action_verify_watch_list_page_loaded(self):
        
        time.sleep(2)
        assert self.driver.title == 'Your Watchlist - IMDb'

        sub_title= self.get_page_subtitle(self.driver).text #text: privet watch list page
        assert sub_title == 'Your Watchlist'
        time.sleep(2)

# this action get the movie name from the coming soon list the first movie, and remove brakets from the name, 
# the function check if the added movie to watchlist have the same name as in the coming soon list
    def action02_find_movie_list_and_check_the_mov_added(self,addedmovi):
        
        time.sleep(2)
        movies_title_elem=[]
        movies_title_elem = self.get_movie_titles(self.driver)
        print(len(movies_title_elem))
        
        movie_names = []
        for movie in movies_title_elem:
            name_title= movie.text
            movie_names.append(name_title)
        print(movie_names)
        
        name_after = addedmovi.strip(" (2021)")
        i=0
        for movie in movie_names:
            if movie in addedmovi:
                assert movie == name_after
                print('movie added to your watch list')
                break
            i=+1
        time.sleep(2)
        

        #self.driver.execute_script("window.scrollTo(0,500)")
        #get all buttons 'add to watch list' check if they all same text and click on the fisrt butn 
    
# click on EDIT link above the watch list 
    def action03_click_on_edit_button(self):
        
        self.get_edit_button(self.driver).click()
        time.sleep(2)