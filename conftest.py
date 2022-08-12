"""This python file provides all the test setup/teardown and other important entities for our testing"""

"Import the necessary library"
from pytest import fixture
from playwright.sync_api import sync_playwright


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

