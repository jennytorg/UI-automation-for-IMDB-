from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


class edit_watchList_imdb:


    edit_form_title = (By.CLASS_NAME, "lister-edit-form")
    setting = (By.ID, 'list-settings')
    DONE = (By.CSS_SELECTOR,"button[class = 'btn-raised btn-raised--primary list-edit-done']")
    check_boxes_path = (By.XPATH, "//input[@type='checkbox'][@class = 'element-check']")
    movie_titles = (By.CLASS_NAME, "lister-item-title")
    #attr class = 'flat-button' when disabled 'flat-button disabled'
    move_item = (By.ID, 'move_items')
    copy_item = (By.ID, 'copy_items')
    delete_item = (By.ID, 'delete_items')

    delete_pop_app = (By.ID, 'delete_items_content')
    delete_link = (By.CSS_SELECTOR,'#delete_items_form div input')



    #'//a[@href="'+url+'"]'
    #“//tag [contains( text(), ‘word’)]”

    def __init__(self,driver):
        self.driver = driver

    def get_edit_form(self,driver):
        return driver.find_element(*edit_watchList_imdb.edit_form_title)#attr class 

    def get_done_button(self,driver):
        return driver.find_element(*edit_watchList_imdb.DONE)

    def get_check_boxes(self,driver):
        return driver.find_elements(*edit_watchList_imdb.check_boxes_path)

    def get_movie_titles(self,driver):
        return driver.find_elements(*edit_watchList_imdb.movie_titles)

    def get_move_to(self,driver):
        return driver.find_element(*edit_watchList_imdb.move_item)

    def get_copy_to(self,driver):
        return driver.find_element(*edit_watchList_imdb.copy_item)

    def get_delete(self,driver):
        return driver.find_element(*edit_watchList_imdb.delete_item)

    def get_delete_popapp(self,driver):
        return driver.find_element(*edit_watchList_imdb.delete_pop_app)

    def get_delete_link(self,driver):
        return driver.find_element(*edit_watchList_imdb.delete_link)


    def action_verify_edit_page(self):
     assert  self.get_edit_form(self.driver).get_attribute('class') == 'lister-edit-form'


    # check the last checkbox in the movie list only if there are 3 movie raws!
    def action02_check_the_last_checkbox(self):
        action=ActionChains(self.driver)

        time.sleep(2)
        checkBoxes=[]
        checkBoxes = self.get_check_boxes(self.driver)
        print(len(checkBoxes))
        
        # simply use is_selected() can yield their Selected status
        [c.is_selected() for c in checkBoxes]
        # to assert they are all unchecked, use not any()
        assert not any([c.is_selected() for c in checkBoxes])

        # for box in checkBoxes:
        #     result = box.is_selected()
        #     if result:
        #         print('checked')
        #     else:
        #         print('unchecked - good')
        #         continue
        
        dele = self.get_delete(self.driver).get_attribute('class')
        assert dele == 'flat-button disabled'

        for box in checkBoxes:

        # click on the last movie checkbos if you have 3 raws in the list
            if checkBoxes.index(box)==2:
                action.move_to_element(box).click().perform()
                time.sleep(1)



    def action03_get_all_movie_names_in_the_list(self):

        movie_names = []
        movie_title_elem=self.get_movie_titles(self.driver)


        for movie in movie_title_elem:
            name_title= movie.text
            movie_names.append(name_title)
        print(movie_names)

        return movie_names

# check if the delete button enabled and click on it
    def action04_click_on_delete_movie(self):
        
        assert self.get_delete(self.driver).is_enabled() ==  True

        
        self.get_delete(self.driver).click()
        time.sleep(2)
        
        popapp_txt = self.get_delete_popapp(self.driver).text
        print(popapp_txt)
        self.get_delete_link(self.driver).click()

        time.sleep(2)
        

        

