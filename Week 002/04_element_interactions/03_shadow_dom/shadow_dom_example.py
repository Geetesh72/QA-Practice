from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.polymer-project.org/")

        shadow_host = page.locator("shop-app")
        shadow_root = shadow_host.evaluate_handle("el=>el.shodowRoot")
        print("Shodow DOM accessed!")

        page.wait_for_timeout(3000)
        browser.close()


if __name__ == "__main__":
    run()


