import requests
from bs4 import BeautifulSoup
import os

URL = "https://worldcup.avatarqn.com/"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

r = requests.get(URL, timeout=20)
html = r.text

keyword = "Đã Kết Thúc"

state_file = "state.txt"

old = ""
if os.path.exists(state_file):
    with open(state_file, "r", encoding="utf-8") as f:
        old = f.read()

new = "closed" if keyword in html else "opened"

if old != new:
    with open(state_file, "w", encoding="utf-8") as f:
        f.write(new)

    if new == "opened":
        text = "🎉 Avatar World Cup đã mở trận mới!"
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": CHAT_ID,
                "text": text
            }
        )
