from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        
        page.locator("input[name='q']").fill("playwright testing")
        page.wait_for_selector("ul[role='listbox'] li")

        suggestions = page.locator("ul[role='listbox'] li span")
        print("Top 5 suggestions:")
        for i in range(min(5, suggestions.count())):
            print(suggestions.nth(i).inner_text())

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()
