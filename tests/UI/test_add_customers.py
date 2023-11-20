import json

import pytest
import re
from pages.AddCustomerPage import Addcustomer
from pages.LoginPage import Login

@pytest.mark.usefixtures('setup')
class Test_002_add_customer():

    test_user = json.load(open(f"testData/test_data.json"))["test_user"]

    @pytest.mark.xdist_group(name="Suit2")
    @pytest.mark.smoke
    @pytest.mark.repeat(1)
    @pytest.mark.parametrize("username, password", [
        (test_user["nop_store_admin"]["username"], test_user["nop_store_admin"]["password"])
    ])
    def test_add_customer_feature(self, username, password, test_data):
        # login into application
        assert username == test_data["test_user"]["nop_store_admin"]["username"]
        assert password == test_data["test_user"]["nop_store_admin"]["password"]
        self.loginPage = Login(self.driver)
        self.loginPage.setUserName(username)
        self.loginPage.setPassword(password)
        self.loginPage.clickLogin()
        assert self.driver.title == "Dashboard / nopCommerce administration", \
            self.loginPage.commonMethods.addAllureScreenShot(self.driver.title)
        # select customer category
        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')
        self.addCustomerPage.clickAddNewButton()
        assert self.driver.title == "Add a new customer / nopCommerce administration", \
            self.addCustomerPage.commonMethods.addAllureScreenShot(self.driver.title)
        self.addCustomerPage.validatePageTitle('Add a new customer')
        self.addCustomerPage.fillUserDetails()
        assert re.search("The new customer has been added successfully.", self.addCustomerPage.getAlertText()), \
            self.addCustomerPage.commonMethods.addAllureScreenShot(self.addCustomerPage.getAlertText())
        self.addCustomerPage.commonMethods.addAllureScreenShot(self.addCustomerPage.getAlertText())