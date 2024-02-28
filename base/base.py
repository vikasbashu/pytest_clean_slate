import allure

class PageBase:

    def __init__(self, driver):
        self.driver = driver
        # self.open()

    @allure.step("Opening main page")
    def open(self):
        self.driver.open()
