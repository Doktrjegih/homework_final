import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.opera.options import Options

from pages.base_page import BasePage


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--bv', action='store')
    parser.addoption('--executor', action='store', default='local')
    parser.addoption('--vnc', action='store_true')
    parser.addoption('--videos', action='store_true')
    parser.addoption('--mobile', action='store_true')  # only for chrome
    parser.addoption('--headless', action='store_true', default=False)


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--bv')
    executor = request.config.getoption('--executor')
    vnc = request.config.getoption('--vnc')
    videos = request.config.getoption('--videos')
    mobile = request.config.getoption('--mobile')
    headless = request.config.getoption('--headless')
    executor_ip = request.config.getoption('--executor')

    if executor != 'local':
        caps = {
            'browserName': browser_name,
            'browserVersion': browser_version,
            'selenoid:options': {'enableVNC': vnc, 'enableVideo': videos},
            'goog:chromeOptions': {},
        }

        if mobile:
            caps['goog:chromeOptions']['mobileEmulation'] = {'deviceName': 'iPhone 5/SE'}

        options = Options()
        if browser_name == 'opera':
            options.add_experimental_option('w3c', True)

        browser = webdriver.Remote(
            command_executor=f'http://{executor_ip}/wd/hub', desired_capabilities=caps, options=options
        )
    else:
        if browser_name == 'chrome':
            print(headless)
            options = ChromeOptions()
            if headless:
                options.headless = headless
                options.add_argument('window-size=1920,1080')
            browser = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            browser = webdriver.Firefox()
        elif browser_name == 'opera':
            browser = webdriver.Opera()
        else:
            raise ValueError('Браузер передан неверно')

    browser.maximize_window()

    def final():
        browser.quit()

    request.addfinalizer(final)
    return browser


@pytest.fixture
def open_site(driver) -> None:  # pylint: disable=redefined-outer-name
    base = BasePage(driver)
    base.open('https://www.python.org/')
