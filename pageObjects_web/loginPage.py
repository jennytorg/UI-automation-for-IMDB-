from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


#find text boxes to sign in user name and password, login btn 

class login:

    

    mdb = (By.XPATH, "//span[contains(text(),'Sign in with IMDb')]")
    email = (By.ID, "ap_email")
    password = (By.ID, "ap_password")
    signin=(By.ID, "signInSubmit")
    sign_option = (By.CSS_SELECTOR, "div[id = 'signin-options'] div h1")

    #'//a[@href="'+url+'"]'
    #“//tag [contains( text(), ‘word’)]”

    def __init__(self,driver):
        self.driver = driver

    def get_title_signin_options(self,driver):
        return driver.find_element(*login.sign_option)

    def get_with_mdb(self,driver):
        return driver.find_element(*login.mdb)

    def get_email(self,driver):
        return driver.find_element(*login.email)

    def get_password(self,driver):
        return driver.find_element(*login.password)

    def get_sign_in(self,driver):
        return driver.find_element(*login.signin)





    def action_click_imdb_signin(self):
        #assert self.driver.title == ''
        text = self.get_title_signin_options(self.driver).text
        assert  text == 'Sign in'
        self.get_with_mdb(self.driver).click()
        time.sleep(2)
    
    def action_fill_the_form_signin(self,usr,passwrd):
        assert self.driver.title == 'IMDb Sign-In'
        self.get_email(self.driver).clear()
        self.get_email(self.driver).send_keys(usr)
        self.get_password(self.driver).clear()
        self.get_password(self.driver).send_keys(passwrd)
        time.sleep(2)
        self.get_sign_in(self.driver).click()
        
