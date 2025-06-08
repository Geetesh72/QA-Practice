from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://news.ycombinator.com/")

        links = page.locator("a.storylink")
        total = links.count()
        print("Total article links:",links.count())

        with open("hn_article.txt","w",encoding="utf-8")as file:
            file.write("Top 5 Hacker News Articles:\n\n")
            for i in range(min(5, total)):
                title = links.nth(i).inner_text()
                print(title)  # Still print to console
                file.write(f"{i + 1}. {title}\n")


       
        page.wait_for_timeout(5000)  # Waits for 10 seconds
        browser.close()

if __name__ =="__main__":
    run()           
