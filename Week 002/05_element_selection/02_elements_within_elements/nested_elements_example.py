from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.w3schools.com/html/html_tables.asp")

        row = page.locator("tr",has = page.locator("td",has_text="Island Trading"))
        print("text matched at row:",row.inner_text())
        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()

