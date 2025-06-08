from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # custom viewport
        context = browser.new_context(
            viewport={'width':375,'height':668}

        )
        page = context.new_page()
        page.goto("https://www.flipkart.com/")
        page.wait_for_timeout(5000)

        browser.close()


if __name__ =="__main__":
    run()