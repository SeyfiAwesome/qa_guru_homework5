import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 10
    browser.driver.maximize_window()
    browser.open('https://demoqa.com/automation-practice-form')

    browser.driver.execute_script("""
    const fixedBan = document.getElementById('fixedban');
    if (fixedBan) fixedBan.remove();

    const footer = document.querySelector('footer');
    if (footer) footer.remove();
    """)

    yield
    browser.quit()
