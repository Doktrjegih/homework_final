from dataclasses import dataclass


@dataclass
class DownloadsPageLocators:
    DOWNLOAD_LATEST_BUTTON: str = (
        '//h1[text()="Download the latest source release"]' '/following-sibling::p/a[@class="button"]'
    )
    RELEASE: str = (
        '//p[text()="Python releases by version number:"]/following-sibling::div'
        '/following-sibling::ol//a[text()="ver-&"]'
    )
