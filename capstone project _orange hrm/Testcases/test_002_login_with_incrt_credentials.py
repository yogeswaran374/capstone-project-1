from selenium import webdriver
from Pageobjects.Loginpage import Login
from Testdata.data import Inputs,Selectors


class Test_002login:

    def test_loginpage_incorrect_password(self, setup):
        self.driver = setup
        self.driver.get(Inputs.base_url)
        self.loginpage = Login(self.driver)
        self.loginpage.setusername(Inputs.username)
        self.loginpage.setpassword(Inputs.incorrect_password)
        self.loginpage.clicklogin()
        act_url = self.driver.current_url
        # self.loginpage.profile_icon()
        # self.loginpage.logout()
        if act_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":

            assert True, "login successfully"
        else:
            assert False, "cannot login due to Incorrect username & password"




