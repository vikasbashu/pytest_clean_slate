from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from helper.webdriver_listener import WebDriverListener
from helper.webdriver_extended import WebDriverExtended
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def setBrowserOptions(browser, mode):
    if browser.casefold() == "firefox":
        options = FirefoxOptions()
    elif browser.casefold() in ["edge", "chromium"]:
        options = EdgeOptions()
    else:
        options = ChromeOptions()
    if mode is None or mode.__contains__('less'):
        options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1325x744')
    options.add_argument('download.default_directory=v1/output/downloads/')
    return options


class DriverFactory:

    @staticmethod
    def fetch_driver(config, browser, mode) -> WebDriverExtended:
        if browser is None:
            browser = config["browser"]
        if browser.casefold() == "firefox":
            driver = WebDriverExtended(
                webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()),
                                  options=setBrowserOptions(browser, mode)),
                WebDriverListener(),
                config)
        elif browser.casefold() in ["edge", "chromium"]:
            driver = WebDriverExtended(
                webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                               options=setBrowserOptions(browser, mode)),
                WebDriverListener(),
                config)

        else:
            driver = WebDriverExtended(
                webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                 options=setBrowserOptions(browser, mode)),
                WebDriverListener(),
                config)

        return driver
