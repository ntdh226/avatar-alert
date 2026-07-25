from playwright.sync_api import sync_playwright

URL = "https://worldcup.avatarqn.com/"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page(
            viewport={"width": 1280, "height": 720}
        )

        print("Đang mở trang...")

        page.goto(URL, wait_until="networkidle", timeout=60000)

        # Chờ thêm vài giây cho JS tải xong
        page.wait_for_timeout(5000)

        print("=" * 80)
        print("HTML SAU KHI JS CHẠY")
        print("=" * 80)

        html = page.content()

        print(html)

        print("=" * 80)
        print("TEXT HIỂN THỊ")
        print("=" * 80)

        print(page.locator("body").inner_text())

        browser.close()


if __name__ == "__main__":
    main()
            
