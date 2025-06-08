from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://mui.com/material-ui/react-button/")

        # Use a role-based or text selector (React renders via JS)
        page.get_by_role("button", name="Contained").click()
        print("Clicked 'Contained' button")

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()
