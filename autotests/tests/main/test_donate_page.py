import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from autotests.pages.page_main.main_page import MainPage


@pytest.mark.xdist_group(name='main')
@allure.parent_suite('Главная страница')
@allure.suite('Проверки главной страницы')
@allure.title('Проверка наличия лого')
@pytest.mark.usefixtures('open_site')
def test_check_logo(driver: WebDriver) -> None:
    main = MainPage(driver)

    main.goto_donate_page()
