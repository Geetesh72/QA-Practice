from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")

        page.frame_locator("#iframeResult").locator("select").select_option("audi")
        print("Audi selected from dropdown")

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()
