"""This python file is about saucedemo menu page, its UI Element and test methods."""

"Import all the necessary libraries"

from Config.config import TestData
import pytest
from playwright.sync_api import Playwright, sync_playwright, Page
from Test_methods.sauceDemo_LoginPage import LoginPage
from Test_methods.BasePage import Base


class MenuPage(Base):
    pass