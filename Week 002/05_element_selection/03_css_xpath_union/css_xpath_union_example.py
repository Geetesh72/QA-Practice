from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wikipedia.org/")

        # CSS Union: Match either English or Español button
        union_locator = page.locator("strong:has-text('English'), strong:has-text('Español')")
        print("Matched button texts:")
        for i in range(union_locator.count()):
            print(union_locator.nth(i).inner_text())

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()
