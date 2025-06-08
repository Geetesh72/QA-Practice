from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.wikipedia.org/")


        # Now use the text selector 
        english_link = page.locator("a[lang]='en'")
        english_link.wait_for()

        english_link.click()

        # Assert that we're on the English Wikipedia
        assert "Wikipedia" in page.title()
       
        page.wait_for_timeout(5000)

        browser.close()


if __name__ =="__main__":
    run()

