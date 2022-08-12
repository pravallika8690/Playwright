"""This python file provides all the necessary methods (APIs) to perform the testing for the
'https://www.saucedemo.com/' website login page """

"Import all the necessary libraries"

from Config.config import TestData
import pytest
from playwright.sync_api import Playwright, sync_playwright


class LoginPage(TestData):

    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

    """Go to base-URL"""

    def webPage_Launch(self, url):
        self.page.goto(url=url)

    """Test method to verify the URL title"""

    def urlTitle(self):
        title = self.page.title()
        print("The URL page title is: ", title)
        return title
