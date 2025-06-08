from playwright.sync_api import sync_playwright
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        try:
            page.locator("button:has-text('Accept all')").click(timeout=3000)
        except:
            pass
        page.wait_for_selector("input[name='q']", timeout=5000)
        page.fill("input[name='q']","Playwright Python")
        page.keyboard.press("Enter")
        page.wait_for_timeout(5000)
        browser.close()


if __name__  == "__main__":
    run()

    
 
