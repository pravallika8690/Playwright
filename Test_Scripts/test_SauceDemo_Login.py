"""This python file provides test cases for Sauce-demo (https://www.saucedemo.com/) website Login page"""

"Import the necessary library files"

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from Test_methods.sauceDemo_LoginPage import *
import conftest
from Config.config import TestData


class TestLoginPage:
    """Test case to verify the URL Title"""

    def test_URL_Title(self, web_launch):
        urlTitle = web_launch.urlTitle()
        assert urlTitle == TestData.urlTitle
