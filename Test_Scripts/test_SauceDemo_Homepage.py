"""This python file provides test cases for Sauce-demo (https://www.saucedemo.com/) website Home page"""

"Import the necessary library files"

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from Test_methods.sauceDemo_HomePage import HomePage
from Config.config import TestData


class TestHomePage:

    """Test case to add items in the cart"""

    def testAddItemToCart(self, home_Page_launch):
        totalItemsInCart = home_Page_launch.addItemToCart()
        assert totalItemsInCart != 0

    def testHomePageLaunch(self, home_Page_launch):
        homePage_Text = home_Page_launch.homePage_launch()
        assert homePage_Text == TestData.homePage_Text, 'HomePage Texts are not same'
