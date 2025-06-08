from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")

        page.frame_locator("iframe[src='default.asp']").locator("a").first.click()

        page.wait_for_timeout(3000)
        browser.close()


if __name__ == "__main__":
    run()