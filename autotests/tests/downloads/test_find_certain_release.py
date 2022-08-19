import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from autotests.pages.navigation.navigation import Navigation
from autotests.pages.navigation.navigation_locators import Pages
from autotests.pages.page_downloads.downloads_page import Downloads


@pytest.mark.xdist_group(name='downloads')
@allure.parent_suite('Главная страница')
@allure.suite('Проверки главной страницы')
@allure.title('Проверка наличия конкретной версии Python')
@pytest.mark.usefixtures('open_site')
def test_download_link(driver: WebDriver) -> None:
    navigation = Navigation(driver)
    downloads = Downloads(driver)

    navigation.goto_page(Pages.DOWNLOADS)
    downloads.check_certain_release(text='Python 3.9.5')
