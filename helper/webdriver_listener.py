import logging
import datetime
from selenium.webdriver.support.events import AbstractEventListener


class WebDriverListener(AbstractEventListener):

    log_fileName = datetime.datetime.now().strftime("%Y-%m-%d")
    logging.basicConfig(level=logging.INFO,
                        filename=f"output/logs/{log_fileName}.log",
                        format="%(asctime)s: %(levelname)s: %(message)s"
                        )

    def __init__(self):
        self.logger = logging.getLogger("selenium")

    def before_navigate_to(self, url: str, driver) -> None:
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url: str, driver) -> None:
        self.logger.info(f"Navigated to {url}")

    def before_find(self, by, value, driver) -> None:
        self.logger.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver) -> None:
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver) -> None:
        self.logger.info(f"Clicking on {element.get_attribute('class')}") if element.get_attribute("text") is None else\
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver) -> None:
        pass
        # self.logger.info(f"{element.get_attribute('class')} clicked") if element.get_attribute("text") is None else\
        #     self.logger.info(f"{element.get_attribute('text')} clicked")

    def before_change_value_of(self, element, driver) -> None:
        self.logger.info(f"Changing {element.get_attribute('text')} value")

    def after_change_value_of(self, element, driver) -> None:
        self.logger.info(f"{element.get_attribute('text')} value changed")

    def before_quit(self, driver) -> None:
        self.logger.info("Quitting Driver")

    def after_quit(self, driver) -> None:
        self.logger.info("Driver quitted")

    def on_exception(self, exception, driver) -> None:
        self.logger.info(exception)
