from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://datatables.net/examples/data_sources/ajax.html")

        page.wait_for_selector("#example")
        rows = page.locator("#example tbody tr")
        print("Total dynamic rows:", rows.count())

        for i in range(min(rows.count(), 5)):
            print(rows.nth(i).inner_text())

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()