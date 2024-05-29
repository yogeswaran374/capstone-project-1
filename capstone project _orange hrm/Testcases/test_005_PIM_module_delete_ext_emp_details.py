from selenium import webdriver
from Pageobjects.Loginpage import Login
from Pageobjects.PIM_module_delete_exist_emp_details import Pim_module_delete_exist_employee
from Testdata.data import Inputs,Selectors
from selenium.webdriver.common.by import By

class Test_005_delete_exist_employee_details:

    def test_PIMpage_delete_exist_emp_details(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.driver.maximize_window()
        self.loginpage = Login(self.driver)
        self.PIM_page_delete_exist = Pim_module_delete_exist_employee(self.driver)
        self.loginpage.setusername(Inputs.username)
        self.loginpage.setpassword(Inputs.password)
        self.loginpage.clicklogin()
        self.PIM_page_delete_exist.pim_module_delete_existing_emp_details(Inputs.firstname)
        self.PIM_page_delete_exist.check_emp_details_deleted_or_not(Inputs.firstname)
        records_element = self.driver.find_element(By.XPATH, Selectors.records)
        print(records_element.text)


        assert  "No Records Found" == records_element.text, "successfully deleted the existing employee details"


