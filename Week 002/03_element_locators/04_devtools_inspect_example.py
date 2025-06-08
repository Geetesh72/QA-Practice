from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,devtools=True)
        page = browser.new_page()
        page.goto("https://www.flipkart.com/")
        page.wait_for_timeout(10000)
        browser.close()

if __name__ =="__main__":
    run()        
