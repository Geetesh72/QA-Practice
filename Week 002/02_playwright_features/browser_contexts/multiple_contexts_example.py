from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context1 = browser.new_context()
        page1  = context1.new_page()
        page1.goto("https://www.flipkart.com/")
        page1.fill("input[name='q']","User First Search")

        # Now Creating Second Browser Context in isolated session

        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://www.flipkart.com/")
        page2.fill("input[name='q']","User Second Search")

        page1.wait_for_timeout(5000)
        page2.wait_for_timeout(5000)


if __name__ =="__main__":
    run()