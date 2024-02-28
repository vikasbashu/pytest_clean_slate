from base.base import PageBase
from locators import getLocators


class SearchCustomer(PageBase):

    table_output_index = {
        'noData': '1',
        'email': "2",
        'name': "3",
        'roles': "4",
        'company': "5",
        'active': "6",
        'edit': "7"
    }
    search_criteria = 'noData'
    search_value = ''
    locators = getLocators('nopCommerce_locators')['searchCustomer']

    def __init__(self ,driver, commonMethods):
        super().__init__(driver)
        self.commonMethods = commonMethods


    def fillEmailField(self, email):
        self.commonMethods.fillLocatorById(self.locators['input_email_id'], email)
        self.search_criteria = "email"
        self.search_value = email

    def fillFirstNameField(self, firstName):
        self.commonMethods.fillLocatorById(self.locators['input_firstName_id'], firstName)
        self.search_criteria = "name"
        self.search_value = firstName

    def fillLastNameField(self, lastName):
        self.commonMethods.fillLocatorById(self.locators['input_lastName_id'], lastName)
        self.search_criteria = "name"
        self.search_value = lastName

    def searchRecords(self):
        self.commonMethods.clickLocatorById(self.locators['button_search_id'])
        # self.commonMethods.clickElement(self.locators['search_pane'])

    def getOutputResult(self):
        self.commonMethods.wait(5)
        return self.commonMethods.getTextFromLocator(self.locators['search_result_xpath'].format(1, self.table_output_index[self.search_criteria]))
