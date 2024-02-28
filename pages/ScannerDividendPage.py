from utils.common_selenium_methods import CommonMethods
from locators.locators import Scanner
from utils.excel_utilities import Excel_Methods
class ScannerDividend:

    def __init__(self, driver):
        self.commonMethods = CommonMethods(driver)
        self.excel = Excel_Methods("output/files/ScannerStocks.xlsx", "Sheet4")

    def get_page_title(self):
        return self.commonMethods.get_title()

    def get_welcome_message(self):
        return self.commonMethods.getTextFromLocator(Scanner.welcome_message_css)

    def get_header_count(self):
        return self.commonMethods.get_element_count(Scanner.table_headers_xpath) // 2

    def fetch_headers(self):
        for i in range(1, self.get_header_count()+1):
            self.excel.write_data(row_num=1, column_num=i, data=self.commonMethods.getTextFromLocator(
                Scanner.get_specific_header(index=i)))

    def fetch_records(self):
        row = 1
        while self.commonMethods.isPresent(Scanner.fetch_records(row=row, col=1), 5):
            for i in range(1, self.get_header_count()+1):
                self.commonMethods.scrollElementToView(Scanner.fetch_records(row=row, col=i))
                self.excel.write_data(row_num=row+1, column_num=i, data=self.commonMethods.getTextFromLocator(
                    Scanner.fetch_records(row=row, col=i)))
            row += 1