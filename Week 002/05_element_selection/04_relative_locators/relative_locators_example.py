from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.w3schools.com/html/html_forms.asp")

        # Find input next to a label using relative relationship
        label = page.locator("label", has_text="First name:")
        input_box = label.locator("xpath=following-sibling::input")
        input_box.fill("John")

        print("Filled input next to 'First name:' label")

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()
