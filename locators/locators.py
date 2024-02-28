from selenium.webdriver.common.by import By


class Scanner:
    welcome_message_css = (By.CSS_SELECTOR, "#screen-info > h1")
    table_headers_xpath = (By.XPATH, "(//table//child::th)")

    @staticmethod
    def get_specific_header(index):
        return (By.XPATH, f"(//table//child::th)[{str(index)}]")

    @staticmethod
    def fetch_records(row, col):
        return (By.XPATH, f"(//table//child::tr[@data-row-company-id > 1][{row}]/td)[{col}]")

