from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    ElementNotVisibleException, InvalidArgumentException, NoAlertPresentException
import time, re
import allure
from allure_commons.types import AttachmentType


class CommonMethods:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    @staticmethod
    def xpathBuilder(attribute, value):
        return f"(//*[@{attribute} = '{value}'])[1]"

    def get_element_count(self, locator):
        return 26
           # len(self.driver.find_elements(locator))

    def fillLocatorById(self, locatorId, value):
        self.driver.find_element(By.ID, locatorId).clear()
        self.driver.find_element(By.ID, locatorId).send_keys(value)

    def fillLocatorByXpath(self, locatorXpath, value):
        self.driver.find_element(By.XPATH, locatorXpath).clear()
        self.driver.find_element(By.XPATH, locatorXpath).send_keys(value)

    def clickLocatorById(self, locatorId):
        self.driver.find_element(By.ID, locatorId).click()

    def waitForVisible(self, locator, time_out):
        assert WebDriverWait(self.driver, time_out).until(
            EC.visibility_of_element_located((By.XPATH, locator))).is_displayed()

    def waitForEnable(self, locator, time_out):
        element = WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable((By.XPATH, locator)))
        assert element.is_enabled()

    def clickElement(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def dontseeElement(self, locator):
        WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def waitForInvisible(self, locator, time_out):
        WebDriverWait(self.driver, time_out).until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def getTextFromLocator(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, locator) if isinstance(locator, str) else locator)).text

    def seeTextOnLocator(self, locator, text):
        assert WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, locator), text))

    def isPresent(self, locator, time_out):
        flag = False
        try:
            element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, locator) if isinstance(locator, str) else locator))
            assert element.is_displayed()
        except TimeoutException:
            flag = False
        except InvalidArgumentException:
            flag = False
        else:
            flag = True
        finally:
            return flag

    def selectValue(self, locator, visible_text):
        element = self.driver.find_element(By.XPATH, locator)
        drp = Select(element)
        drp.select_by_visible_text(visible_text)

    def wait(self, time_out):
        time.sleep(int(time_out))

    def containsText(self, super_string, sub_string):
        assert re.search(sub_string, super_string)

    def fillField(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator))).clear().send_keys(
            text)

    def pressKey(self, key):
        """Function created to press keyboard keys"""
        if key == "Enter":
            self.action.send_keys(Keys.ENTER)
        elif key == 'Backspace':
            self.action.send_keys(Keys.BACKSPACE)
        self.action.perform()

    def verifyTitle(self, title):
        assert self.driver.title == title

    def get_title(self):
        return self.driver.title

    def switchToIframe(self, locator):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, locator))

    def switchToParent(self):
        self.driver.switch_to.default_content()

    def acceptAlerts(self):
        try:
            self.driver.switch_to.alert().accept()
        except NoAlertPresentException:
            pass

    def dismissAlert(self):
        try:
            self.driver.switch_to.alert().dismiss()
        except NoAlertPresentException:
            pass

    def scrollTo(self, start_value, end_value):
        """Scroll down the page by pixel to pixel"""
        self.driver.execute_script("window.scrollBy({}, {})".format(start_value, end_value), "")

    def scrollElementToView(self, locator):
        """Scroll down the page till the element is visible"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, locator) if isinstance(locator, str) else locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scrollTillEnd(self):
        """Scroll down page till end"""
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def scrollToUp(self):
        """Scroll at the top"""
        self.driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")

    def doubleClick(self, locator):
        self.action.double_click(self.driver.find_element(By.XPATH, locator)).perform()

    def rightClick(self, locator):
        self.action.context_click(self.driver.find_element(By.XPATH, locator)).perform()

    def dragAndDrop(self, source_locator, target_locator):
        self.action.drag_and_drop(self.driver.find_element(By.XPATH, source_locator),
                                  self.driver.find_element(By.XPATH, target_locator)).perform()

    def uploadFile(self, locator, file_name):
        self.driver.find_element(By.XPATH, locator).send_keys("testData/sampleFiles/{}".format(file_name))

    def closeBrowser(self):
        self.driver.close()

    def closeAllBrowser(self):
        self.driver.quit()

    def getCurrentWindowHandle(self):
        """Return the handle value of current opened window"""
        return self.driver.current_window_handle

    def getWindowHandle(self):
        """Return a list of window handles of all opened windows"""
        temp_list = self.driver.window_handles
        return temp_list

    def takeScreenShot(self, file_name):
        self.driver.save_screenshot(str("Screenshots/{}.png").format(file_name))

    def clearField(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator))).clear()

    def datePicker(self, locator, date):
        self.clearField(locator)
        self.fillField(locator, date)
        self.wait(1)
        self.pressKey('Enter')

    def selectRadioOption(self, option):
        self.waitForVisible("(//span[text()=\"{}\"]/../../input)[1]".format(option), 5)
        self.clickElement("(//span[text()=\"{}\"]/../../input)[1]".format(option))

    def clickLink(self, link):
        locator = "(//*[contains(text(), \"{}\")])[1]".format(link)
        self.waitForEnable(locator, 5)
        self.clickElement(locator)

    def seePopUp(self, title):
        """Validate popup title"""
        locator = "(//h3[contains(text(), \"{}\")])[1]".format(title)
        self.waitForVisible(locator, 5)

    def seeToastMessage(self, message):
        """Validate the toast message and click on its close button in order to save time"""
        locator = "(//*[contains(text(), \"{}\")])[1]".format(message)
        self.waitForVisible(locator, 10)
        close_toast_button = "(//*[contains(text(), \"{}\")]/following::button)[1]".format(message)
        self.clickElement(close_toast_button)
        self.dontseeElement(locator)

    def addAllureScreenShot(self, file_name):
        allure.attach(self.driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)

    def pressButton(self, label):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(//button[@type='submit'and @name='{}'])[1]".format(label)))).click()
