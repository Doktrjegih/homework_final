import allure

from pages.base_page import BasePage
from pages.navigation.navigation_locators import OtherPagesLocators
from pages.page_main.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Проверить, что поле поиска присутствует на главной странице')
    def check_search_field(self) -> None:
        if not self.is_element_present(MainPageLocators.SEARCH_INPUT):
            self.fail('Поле поиска отсутствует на главной странице')

    @allure.step("Выполнить поиск по запросу '{text}' на главной странице")
    def find_with_search(self, text: str) -> None:
        self.input_text(MainPageLocators.SEARCH_INPUT, text=text)
        self.click(MainPageLocators.SEARCH_SUBMIT_BUTTON)

    @allure.step('Найти лого на главной странице')
    def check_logo(self) -> None:
        if not self.is_element_present(MainPageLocators.LOGO):
            self.fail('Лого отсутствует на главной странице')

    @allure.step('Перейти на страницу донатов')
    def goto_donate_page(self) -> None:
        self.click(MainPageLocators.DONATE_BUTTON)
        if not self.is_element_present(OtherPagesLocators.DONATE_LOGO):
            self.fail('Перехода на страницу донатов не произошло за {timeout} сек')

    @allure.step('Перейти на страницу документации')
    def goto_documentation_page(self) -> None:
        self.click(MainPageLocators.DOCUMENTATION)
        if not self.is_element_present(OtherPagesLocators.DOCUMENTATION_HEAD):
            self.fail('Перехода на страницу документации не произошло за {timeout} сек')
