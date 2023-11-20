from utils.common_selenium_methods import CommonMethods as CommonFunctions
from locators import getLocators
from base.base import PageBase


class Login(PageBase):

    locators = getLocators('nopCommerce_locators')['Login']

    def __init__(self, driver):
        super().__init__(driver)
        self.commonMethods = CommonFunctions(driver)

    def setUserName(self, username):
        self.commonMethods.fillLocatorById(self.locators['textbox_username_id'], username)

    def setPassword(self, password):
        self.commonMethods.fillLocatorById(self.locators['textbox_password_id'], password)

    def clickLogin(self):
        self.commonMethods.clickElement(self.locators['button_login_xpath'])

    def clickLogout(self):
        self.commonMethods.clickElement(self.locators['link_logout_linkText'])

    def checkFailedLoginErrorMessage(self):
        assert self.commonMethods.getTextFromLocator(self.locators['text_errorMessage_xpath']) == "Login was unsuccessful. Please correct the errors and try again. "
