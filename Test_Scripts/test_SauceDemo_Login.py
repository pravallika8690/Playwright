"""This python file provides test cases for Sauce-demo (https://www.saucedemo.com/) website Login page"""

"Import the necessary library files"

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from Test_methods.sauceDemo_LoginPage import *


class TestLoginPage:
    """Test case to verify the URL Title"""

    def test_URL_Title(self, page):
        login_page = LoginPage(base_url=TestData.baseURL)
        login_page.urlTitle()
        expect(page).to_have_title(TestData.urlTitle), 'Title is mismatching'
