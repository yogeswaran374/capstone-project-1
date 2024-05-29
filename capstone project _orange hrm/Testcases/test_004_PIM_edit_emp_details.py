from selenium import webdriver
from Pageobjects.Loginpage import Login
from Pageobjects.PIM_module_edit_emp_details import Pim_module_edit_employee
from Testdata.data import Inputs,Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_004_edit_employee_details:


    def test_PIMpage_edit_emp_details(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.driver.maximize_window()
        self.loginpage = Login(self.driver)
        self.PIM_page_edit = Pim_module_edit_employee(self.driver)
        self.loginpage.setusername(Inputs.username)
        self.loginpage.setpassword(Inputs.password)
        self.loginpage.clicklogin()
        self.PIM_page_edit.pim_module_edit_emp_details(Inputs.firstname,Inputs.updated_other_id)

        print("employee details edited successfully")


