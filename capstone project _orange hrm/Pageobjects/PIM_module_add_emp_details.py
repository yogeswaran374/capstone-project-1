from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from Pageobjects.Loginpage import Login
from Testdata.data import Inputs, Selectors

class Pim_module_Add_employee:


    def __init__(self, driver):
        self.driver = driver


    def pim_module_add_new_employee(self,firstname, middlename, lastname):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.PIM_icon_abs_xpath))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.Add_button_xpath))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.text_box_firstname_xpath))).send_keys(firstname)
        self.driver.find_element(By.XPATH, Selectors.text_box_middlename_xpath).send_keys(middlename)
        self.driver.find_element(By.XPATH, Selectors.text_box_lastname_xpath).send_keys(lastname)
        self.driver.find_element(By.XPATH, Selectors.save_button_xpath).click()

    def personal_details_filling(self, otherid):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.text_box_other_id_absxpath))).send_keys(otherid)
        self.driver.find_element(By.XPATH, Selectors.gender_radio_button_absxpath).click()
        self.driver.execute_script('window.scrollBy(0, 200)')
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.save_personal_details_button_abs_xpath))).click()













