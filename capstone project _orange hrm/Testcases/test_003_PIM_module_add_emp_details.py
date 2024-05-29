import time

from selenium import webdriver
from Pageobjects.Loginpage import Login
from Pageobjects.PIM_module_add_emp_details import Pim_module_Add_employee
from Testdata.data import Inputs,Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_003_add_employee_details:

    # def test_pimpage(self,setup):
    #     self.driver = setup
    #     self.driver.get(Inputs.base_url)
    #     self.loginpage = Login(self.driver)
    #     self.PIM_page = Pim_module_Add_employee(self.driver)
    #     self.loginpage.setusername(Inputs.username)
    #     self.loginpage.setpassword(Inputs.password)
    #     self.loginpage.clicklogin()
    #     self.PIM_page.pim_module_add_new_employee(Inputs.firstname,Inputs.middlename, Inputs.lastname)
    #     if "Personal Details" in self.driver.current_url:
    #         assert "successfully able to add new employee details"
    #
    #     else:
    #         assert "not able to add new employee details"

    def test_personal_details_page(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.driver.maximize_window()
        self.loginpage = Login(self.driver)
        self.PIM_page = Pim_module_Add_employee(self.driver)
        self.loginpage.setusername(Inputs.username)
        self.loginpage.setpassword(Inputs.password)
        self.loginpage.clicklogin()
        self.PIM_page.pim_module_add_new_employee(Inputs.firstname,Inputs.middlename, Inputs.lastname)
        self.PIM_page.personal_details_filling(Inputs.otherid)

        wait = WebDriverWait(setup, 10)

        lable_element = wait.until(EC.visibility_of_element_located((By.XPATH, Selectors.lable_element)))


        assert "Personal Details" == lable_element.text




