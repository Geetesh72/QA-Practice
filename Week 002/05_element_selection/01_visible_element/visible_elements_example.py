from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

        #show and hide
        show_button = page.locator("button",has_text="Toggle Hide and Show")
        show_button.click()

        paragraph = page.locator("#myDIV")
        if paragraph.is_visible():
            print("Paragraph is visible")
        else:
            print("Paragraph is hidden")   


        page.wait_for_timeout(3000)
        browser.close()


if __name__ == "__main__":
    run()


