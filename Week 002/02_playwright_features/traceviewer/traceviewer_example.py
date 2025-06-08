from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        # trace starts
        context.tracing.start(screenshots=True,snapshots=True,sources=True)
        page = context.new_page()
        page.goto("https://www.flipkart.com/")
        page.click("text=More Information")

        # stop & save

        context.tracing.stop(path="trace.zip")

        print("Trace saved as trace.zip.Open with playwright show-trace trace.zip")
        browser.close()


if __name__ =="__main__":
    run()

