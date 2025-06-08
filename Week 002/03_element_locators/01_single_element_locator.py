from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wikipedia.org/")
        page.locator("input[name='search']").fill("Playwright Python")
        page.locator("button[type='submit']").click()
        page.wait_for_timeout(5000)
        browser.close()



if __name__ =="__main__":
    run()
