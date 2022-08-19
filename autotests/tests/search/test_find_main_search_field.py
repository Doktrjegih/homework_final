import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from autotests.pages.page_main.main_page import MainPage


@pytest.mark.xdist_group(name='search')
@allure.parent_suite('Главная страница')
@allure.suite('Проверки главной страницы')
@allure.title('Проверка наличия поисковой строки на главной странице')
@pytest.mark.usefixtures('open_site')
def test_find_search_field(driver: WebDriver) -> None:
    main = MainPage(driver)

    main.check_search_field()
