import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.page_main.main_page import MainPage
from pages.page_search.search_page import SearchPage


@pytest.mark.xdist_group(name='search')
@allure.parent_suite('Главная страница')
@allure.suite('Проверки главной страницы')
@allure.title('Проверка пустого поиска')
@pytest.mark.usefixtures('open_site')
def test_empty_search(driver: WebDriver) -> None:
    main = MainPage(driver)
    search = SearchPage(driver)

    main.find_with_search(text='')
    search.check_results_not_present()
