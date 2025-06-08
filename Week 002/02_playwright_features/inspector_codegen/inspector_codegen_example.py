from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Lauch browser with headless 
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )
        page = context.new_page()
        
        page.goto("https://www.flipkart.com/")
        page.wait_for_timeout(30000)

        try:
            page.locator("button:has-text('✕')").click(timeout=3000)
        except:
            pass

        page.wait_for_timeout(3000)

        context.tracing.stop(path="trace.zip")
        browser.close()
        print("Trace saved as trace.zip")


if __name__ == "__main__":
    run()

