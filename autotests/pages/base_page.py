import time
from typing import List

import allure
import pytest
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    @allure.step('Открыть url {ip}')
    def open(self, ip: str) -> None:
        self._driver.get(ip)

    @allure.step('Проверить, есть ли элемент: {locator}')
    def is_element_present(self, locator: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self._driver, timeout=timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            return False
        return True

    @allure.step('Найти элементы: {locator}')
    def find_elements(self, locator: str, timeout: int = 5) -> List:
        try:
            return WebDriverWait(self._driver, timeout=timeout).until(
                EC.visibility_of_any_elements_located((By.XPATH, locator))
            )
        except TimeoutException:
            return []

    @allure.step('Найти элемент: {locator}')
    def find_element(self, locator: str, timeout: int = 5) -> WebElement:
        try:
            element = WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            self.fail(f'Элемент {locator} не появился за {timeout} секунд')
        return element

    @allure.step('Нажать на элемент: {locator}')
    def click(self, locator: str, timeout: int = 5, delay: float = 0.1) -> None:
        element = self.find_element(locator=locator, timeout=timeout)
        time.sleep(delay)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.fail(f'Элемент {locator} перекрыт другим элементом')

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def input_text(self, locator: str, text: str, timeout: int = 5, delay: float = 0.1) -> None:
        element = self.find_element(locator=locator, timeout=timeout)
        time.sleep(delay)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def attach_screenshot_to_report(self) -> None:
        allure.attach(
            name=self._driver.session_id,
            body=self._driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )

    def fail(self, error_text: str) -> None:
        self.attach_screenshot_to_report()
        pytest.fail(error_text)
