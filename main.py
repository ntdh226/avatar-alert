from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://worldcup.avatarqn.com/", wait_until="networkidle")
    page.wait_for_timeout(5000)

    print("===== TEXT =====")
    print(page.locator("body").inner_text())

    browser.close()
