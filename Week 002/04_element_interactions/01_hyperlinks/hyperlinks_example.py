from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://news.ycombinator.com/")

        links = page.locator("a")
        total_links = links.count()

        with open("links_output.txt","w",encoding="utf-8") as file:
            file.write(f"Total links: {total_links}\n\n")
            for i in range (min(5,total_links)):
                href = links.nth(i).get_attribute("href")
                file.write(f"{i+1}.{href}\n")

             
    
      

        page.wait_for_timeout(3000)
        browser.close()    


if __name__ == "__main__":
    run()