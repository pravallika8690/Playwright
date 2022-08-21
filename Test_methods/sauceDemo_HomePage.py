"""This python file provides all the necessary methods (APIs) to perform the testing for the
'https://www.saucedemo.com/' website login page """

"Import all the necessary libraries"

from Config.config import TestData
import pytest
from playwright.sync_api import Playwright, sync_playwright, Page
from Test_methods.sauceDemo_LoginPage import LoginPage
from Test_methods.BasePage import Base


class HomePage(Base):
    """Creating variables for web-elements present in the home page"""

    sauceLab_BackPack_Text = "[data-test=\"add-to-cart-sauce-labs-backpack\"]"
    cart_Icon = "#shopping_cart_container a"
    cartItem = "a:has-text(\"1\")"
    product_text = "text=Products"

    def homePage(self, page: Page):
        self.page = page

    """def __init__(self, plywr: Playwright, base_url: str, headless=False):
        self.browser = plywr.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url"""

    """Test method to add item in the cart"""

    def addItemToCart(self):
        num_of_Items_in_Cart = self.page.text_content(self.sauceLab_BackPack_Text)
        print("Number of Items in the cart: ", num_of_Items_in_Cart)
        # self.page.click(self.sauceLab_BackPack_Text)

    """Test method to read homepage title (Products)"""

    def homePage_launch(self):
        text = self.page.text_content(self.product_text)
        print("The home page text is: ", text)
        return text
