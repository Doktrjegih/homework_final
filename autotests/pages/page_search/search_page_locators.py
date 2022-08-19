from dataclasses import dataclass


@dataclass
class SearchPageLocators:
    SEARCH_INPUT: str = '//h2[text()="Search Python.org"]/following-sibling::form//input[@type="text"]'
    SEARCH_RESULT: str = '//ul[@class="list-recent-events menu"]//li'
    SEARCH_SUBMIT: str = '//input[@type="submit"]'
    NO_RESULTS: str = '//p[text()="No results found."]'
