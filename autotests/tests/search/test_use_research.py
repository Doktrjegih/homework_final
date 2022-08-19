import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from autotests.pages.page_main.main_page import MainPage
from autotests.pages.page_search.search_page import SearchPage


@pytest.mark.xdist_group(name='search')
@allure.parent_suite('Главная страница')
@allure.suite('Проверки главной страницы')
@allure.title('Проверка работы поисковой строки')
@pytest.mark.usefixtures('open_site')
def test_use_search(driver: WebDriver) -> None:
    main = MainPage(driver)
    search = SearchPage(driver)

    main.find_with_search(text='qweqwe')
    search.check_results_not_present()
    search.find_on_search_page(text='python')
    search.check_results_present()
