from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser  = p.chromium.launch(headless=False)

        context = browser.new_context(
            viewport={'width':1920,'height':1080}
        )

        page = context.new_page()
        page.goto("https://www.flipkart.com/")
        page.wait_for_timeout(5000)

        browser.close()



if __name__ =="__main__":
    run()        




