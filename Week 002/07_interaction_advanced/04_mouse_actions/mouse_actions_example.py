from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demoqa.com/buttons")

        # Double Click
        double_click_btn = page.locator("#doubleClickBtn")
        double_click_btn.dblclick()

        # Right Click
        right_click_btn = page.locator("#rightClickBtn")
        right_click_btn.click(button="right")

        # Single Click
        click_btn = page.locator("text=Click Me")
        click_btn.click()

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()
