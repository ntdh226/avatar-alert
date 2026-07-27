from playwright.sync_api import sync_playwright

URL = "https://www.facebook.com/Avatar.CFS"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(5000)

    print(page.locator("body").inner_text())

    browser.close()
