import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from Pageobjects.Loginpage import Login
from Testdata.data import Inputs, Selectors


class Pim_module_delete_exist_employee:

    def __init__(self, driver):
        self.driver = driver


    def pim_module_delete_existing_emp_details(self, firstname):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.PIM_icon_abs_xpath))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.textbox_emp_name_absxpath))).clear()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.textbox_emp_name_absxpath))).send_keys(firstname)
        self.driver.find_element(By.XPATH, Selectors.search_button_absxpath).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.delete_existing_emp_details_absxpath))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.popup_yes_button_xpath))).click()

    def check_emp_details_deleted_or_not(self,firstname):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.PIM_icon_abs_xpath))).click()
        # self.driver.find_element(By.XPATH, Selectors.textbox_emp_name_absxpath).clear()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.textbox_emp_name_absxpath))).send_keys(firstname)
        self.driver.find_element(By.XPATH, Selectors.search_button_absxpath).click()

        time.sleep(5)












