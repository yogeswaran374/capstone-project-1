
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Testdata.data import Inputs, Selectors

class Login:


    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,Selectors.textbox_username_xpath))).send_keys(username)


    def setpassword(self,password):
        self.driver.find_element(By.XPATH, Selectors.textbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, Selectors.button_login_xpath).click()

    def profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.profile_icon))).click()

    def logout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Selectors.logout))).click()






