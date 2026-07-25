from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://worldcup.avatarqn.com/"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)
    page.wait_for_timeout(5000)

    text = page.locator("body").inner_text()

    browser.close()

    if "Đã Kết Thúc" in text:
        print("Đang test Telegram...")
send("✅ Test thành công từ GitHub Actions")

            
