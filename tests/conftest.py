import json
from config.driver_factory import DriverFactory
import pytest
from utils.common_selenium_methods import CommonMethods
import requests

@pytest.fixture(scope='class')
def test_data(request):
    with open(f'testData/test_data.json') as f:
        test_data = json.load(f)
    return test_data


def pytest_addoption(parser):
    """This will get the value from CLI/hooks"""
    parser.addoption("--browser")
    parser.addoption("--mode")
    parser.addoption("--env", default="qa")


@pytest.fixture(scope='class')
def browser(request):
    """This will return the browser value to setup method"""
    return request.config.getoption("--browser")


@pytest.fixture(scope='class')
def mode(request):
    """This will return the browser visibility pass with --mode flag"""
    return request.config.getoption("--mode")


@pytest.fixture(scope='session')
def config():
    """This will load the setup from config file"""
    return json.load(open(f"config.json"))

@pytest.fixture(scope='class')
def environment(request, config):
    """This will return the environment value pass with --env flag"""
    env = None
    try:
        env = config['env'][request.config.getoption("--env").casefold()]
    except KeyError:
        env = config['env']['qa']
    finally:
        return env


@pytest.fixture(scope='class')
def setup(request, config, browser, mode, environment):
    """This will initiate the driver object with provided configuration"""
    driver = DriverFactory.fetch_driver(config, browser, mode)
    driver.implicitly_wait(config["timeout"])
    driver.maximize_window()
    driver.get(environment['scanner'] if str(request.cls).__contains__("scanner") else environment["base_url"])
    request.cls.driver = driver
    request.cls.commonMethods = CommonMethods(driver)
    before_failed = request.session.testsfailed
    yield
    driver.quit()

@pytest.fixture(autouse=False)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
