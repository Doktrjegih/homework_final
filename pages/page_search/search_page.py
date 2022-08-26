import allure

from pages.base_page import BasePage
from pages.page_search.search_page_locators import SearchPageLocators


class SearchPage(BasePage):
    @allure.step('Проверить наличие результатов поиска')
    def check_results_present(self) -> None:
        if len(self.find_elements(SearchPageLocators.SEARCH_RESULT)) < 1:
            self.fail('Результаты поиска отсутствуют')

    @allure.step('Проверить отсутствия результатов поиска')
    def check_results_not_present(self) -> None:
        if len(self.find_elements(SearchPageLocators.SEARCH_RESULT)) != 0:
            self.fail('Результаты поиска присутствуют')
        if not self.is_element_present(SearchPageLocators.NO_RESULTS):
            self.fail('Нет сообщения "No results found"')

    @allure.step("Найти '{text}' используя поиск на странице поиска")
    def find_on_search_page(self, text: str) -> None:
        self.input_text(SearchPageLocators.SEARCH_INPUT, text=text)
        self.click(SearchPageLocators.SEARCH_SUBMIT)
