from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from Pageobjects.Loginpage import Login
from Testdata.data import Inputs, Selectors


class Pim_module_edit_employee:

    def __init__(self, driver):
        self.driver = driver

    def pim_module_edit_emp_details(self, firstname,updated_other_id):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.PIM_icon_abs_xpath))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.textbox_emp_name_absxpath))).send_keys(firstname)
        self.driver.find_element(By.XPATH, Selectors.search_button_absxpath).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.Edit_icon_absxpath))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.text_box_other_id_absxpath))).clear()
        self.driver.find_element(By.XPATH, Selectors.text_box_other_id_absxpath).send_keys(updated_other_id)
        self.driver.execute_script('window.scrollBy(0, 200)')
        wait.until(EC.element_to_be_clickable((By.XPATH, Selectors.update_otherid_save_button_absxpath))).click()












