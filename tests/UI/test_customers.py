import json
import allure
import pytest
import re
from pages.AddCustomerPage import Addcustomer
from pages.SearchCustomerPage import SearchCustomer
from pages.LoginPage import Login

loggedIn = False

@pytest.mark.xdist_group(name="Suit2")
@pytest.mark.regression
@pytest.mark.usefixtures('setup')
class Test_002_Customer:
    test_user = json.load(open(f"testData/test_data.json"))["test_user"]


    @pytest.fixture()
    def login(self, test_data):
        global loggedIn
        if not loggedIn:
            self.loginPage = Login(self.driver)
            self.loginPage.setUserName(test_data["test_user"]["nop_store_admin"]["username"])
            self.loginPage.setPassword(test_data["test_user"]["nop_store_admin"]["password"])
            self.loginPage.clickLogin()
            assert self.driver.title == "Dashboard / nopCommerce administration", self.driver.save_screenshot(
                str('Screenshots/{}.png'.format(self.driver.title)))
            loggedIn = True

    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password", [
        (test_user["nop_store_admin"]["username"], test_user["nop_store_admin"]["password"])
    ])
    @allure.title("Test the add customer flow")
    @allure.description("To make sure admin can add users by filling mandatory fields")
    def test_add_customer_feature(self, username, password, test_data, login):
        # login into application
        assert username == test_data["test_user"]["nop_store_admin"]["username"]
        assert password == test_data["test_user"]["nop_store_admin"]["password"]
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

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @allure.title("Test the search by email flow")
    @allure.description("To make sure admin can filter customers by email")
    def test_search_customer_by_email(self, test_data, login):
        search_value = test_data["test_user"]["user_details"]["email"]
        # Navigate to customer page
        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')
        # search customer

        self.customerPage = SearchCustomer(self.driver, self.commonMethods)
        self.customerPage.fillEmailField(search_value)
        self.customerPage.searchRecords()
        self.result = self.customerPage.getOutputResult()

        if search_value in self.result:
            assert True
        else:
            self.customerPage.commonMethods.addAllureScreenShot(search_value)
            assert "No data available in table" == self.result
            assert False

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.title("Test the search by firstName flow")
    @allure.description("To make sure admin can filter customers by firstName")
    def test_search_customer_by_firstName(self, test_data, login):
        search_value = test_data["test_user"]["user_details"]["username"].split(" ")[0]
        # Navigate to customer page
        self.addCustomerPage = Addcustomer(self.driver)
        self.addCustomerPage.selectSubCategory('Customer')

        # search customer

        self.customerPage = SearchCustomer(self.driver, self.commonMethods)
        self.customerPage.fillFirstNameField(search_value)
        self.customerPage.searchRecords()
        self.result = self.customerPage.getOutputResult()

        if search_value in self.result:
            assert True
        else:
            self.customerPage.commonMethods.addAllureScreenShot(search_value)
            assert "No data available in table" == self.result
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip("Will implement this later")
    @pytest.mark.sanity
    @allure.title("Test the search by lastName flow")
    @allure.description("To make sure admin can filter customers by lastName")
    def test_search_customer_by_lastName(self, test_data):
        search_value = test_data["test_user"]["user_details"]["username"].split(" ")[1]
        pass
