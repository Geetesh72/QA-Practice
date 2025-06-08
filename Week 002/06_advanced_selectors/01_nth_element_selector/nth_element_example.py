from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://news.ycombinator.com/")

        titles = page.locator("a.storylink")  # all story titles
        print("First 3 Hacker News article titles:")
        for i in range(min(3, titles.count())):
            print(titles.nth(i).inner_text())

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    run()
