import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")

def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_google(browser):
    page = browser.new_page()
    page.goto("https://www.google.com/")
    try:
        page.locator("button:has-text('Accept all')").click(timeout=3000)
    except:
        pass 

    page.wait_for_selector("input[name='q']",timeout=5000)
    page.fill("input[name='g']","Tyfone")
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    assert "Tyfone" in page.title()
    
