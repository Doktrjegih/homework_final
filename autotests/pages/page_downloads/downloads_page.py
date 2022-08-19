import allure

from autotests.pages.base_page import BasePage
from autotests.pages.page_downloads.downloads_page_locators import DownloadsPageLocators


class Downloads(BasePage):
    @allure.step('Проверить наличие кнопки загрузки последней версии Python')
    def check_download_latest_button(self) -> None:
        if not self.is_element_present(DownloadsPageLocators.DOWNLOAD_LATEST_BUTTON):
            self.fail('Кнопка загрузки последней версии Python отсутствует')

    @allure.step('Найти в таблице старых версий Python: {text}')
    def check_certain_release(self, text: str) -> None:
        if not self.is_element_present(DownloadsPageLocators.RELEASE.replace('ver-&', text)):
            self.fail(f'Запись "{text}" отсутствует в таблице старых версий Python')
