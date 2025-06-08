from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.w3schools.com/html/html_tables.asp")

        # Get the table rows
        rows = page.locator("#customers tr")
        print("Total rows:", rows.count())

        for i in range(rows.count()):
            print(rows.nth(i).inner_text())

        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    run()
