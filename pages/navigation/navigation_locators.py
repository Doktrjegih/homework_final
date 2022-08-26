from dataclasses import dataclass


@dataclass
class Pages:
    ABOUT: str = 'about'
    DOWNLOADS: str = 'downloads'
    DOCUMENTATION: str = 'documentation'
    COMMUNITY: str = 'community'
    STORIES: str = 'success-stories'
    NEWS: str = 'news'
    EVENTS: str = 'events'


@dataclass
class NavigationLocators:
    MENU_BAR: str = '//ul[@class="navigation menu" and @role="menubar"]'

    ABOUT: str = '//li[@id="about"]'
    DOWNLOADS: str = '//li[@id="downloads"]'
    DOCUMENTATION: str = '//li[@id="documentation"]'
    COMMUNITY: str = '//li[@id="community"]'
    STORIES: str = '//li[@id="success-stories"]'
    NEWS: str = '//li[@id="news"]'
    EVENTS: str = '//li[@id="events"]'


@dataclass
class OtherPagesLocators:
    DONATE_LOGO: str = '//img[@alt="Python Software Foundation"]'
    DOCUMENTATION_HEAD: str = '//h1[contains(text(), "documentation")]'
