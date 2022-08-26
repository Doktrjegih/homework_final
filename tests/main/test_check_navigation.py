import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.navigation.navigation import Navigation
from pages.navigation.navigation_locators import NavigationLocators, Pages


@pytest.mark.xdist_group(name='main')
@allure.parent_suite('Главная страница')
@allure.suite('Проверки главной страницы')
@allure.title('Проверка отображения меню на каждой странице бар-меню')
@pytest.mark.usefixtures('open_site')
@pytest.mark.parametrize(
    'page',
    (Pages.ABOUT, Pages.DOWNLOADS, Pages.DOCUMENTATION, Pages.COMMUNITY, Pages.STORIES, Pages.NEWS, Pages.EVENTS),
)
def test_check_navigation(driver: WebDriver, page: Pages) -> None:
    navigation = Navigation(driver)

    navigation.goto_page(page)
    assert navigation.is_element_present(NavigationLocators.MENU_BAR)
