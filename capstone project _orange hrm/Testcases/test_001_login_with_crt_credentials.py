from selenium import webdriver
from Pageobjects.Loginpage import Login
from Testdata.data import Inputs,Selectors


class Test_001_login:

    def test_homepage(self,setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "OrangeHRM":
            assert True ,"Login successfully"
        else:
            assert False


    def test_loginpage_correct_password(self, setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.loginpage = Login(self.driver)
        self.loginpage.setusername(Inputs.username)
        self.loginpage.setpassword(Inputs.password)
        self.loginpage.clicklogin()
        act_url = self.driver.current_url

        if act_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":

            assert True ,"login successfully"
        else:
            assert False ,"cannot login due to Incorrect username & password"





