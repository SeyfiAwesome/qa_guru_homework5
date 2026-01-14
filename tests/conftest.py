import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_management():
    browser.driver.maximize_window()
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()

