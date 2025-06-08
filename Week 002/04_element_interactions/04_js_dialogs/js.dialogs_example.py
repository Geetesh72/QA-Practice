from playwright.sync_api  import sync_playwright

def run():
    def handle_dailog(dialog):
        print("Dailog message:",dialog.message)
        dialog.accept("Playwright User")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()


        page.on("dialog",handle_dailog)
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")
        page.click("text=click for JS Prompt")

        page.wait_for_timeout(3000)
        browser.close()


if __name__ == "__main__":
    run()

