import allure

from autotests.pages.base_page import BasePage
from autotests.pages.navigation.navigation_locators import NavigationLocators


class Navigation(BasePage):
    @allure.step('Перейти на страницу: {page_name}')
    def goto_page(self, page_name: str) -> None:
        if page_name == 'about':
            self.click(NavigationLocators.ABOUT)
        if page_name == 'downloads':
            self.click(NavigationLocators.DOWNLOADS)
        if page_name == 'documentation':
            self.click(NavigationLocators.DOCUMENTATION)
        if page_name == 'community':
            self.click(NavigationLocators.COMMUNITY)
        if page_name == 'success-stories':
            self.click(NavigationLocators.STORIES)
        if page_name == 'news':
            self.click(NavigationLocators.NEWS)
        if page_name == 'events':
            self.click(NavigationLocators.EVENTS)
