from dataclasses import dataclass


@dataclass
class MainPageLocators:
    SEARCH_INPUT: str = '//input'
    SEARCH_SUBMIT_BUTTON: str = '//button'
    LOGO: str = '//img[@class="python-logo"]'
    DONATE_BUTTON: str = '//a[text()="Donate"]'
    DOCUMENTATION: str = '//a[@title="Python Documentation"]'
