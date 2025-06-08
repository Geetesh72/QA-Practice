from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")  # 

        
        heading = page.locator("xpath=//h1")
        print("Heading Text:", heading.inner_text())

        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    run()