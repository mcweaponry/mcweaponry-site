from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Desktop
        page = browser.new_page(viewport={'width': 1280, 'height': 720})
        page.goto('http://localhost:5173/')
        page.screenshot(path='jules-scratch/verification/desktop.png', full_page=True)

        # Mobile
        page = browser.new_page(viewport={'width': 375, 'height': 667})
        page.goto('http://localhost:5173/')
        page.screenshot(path='jules-scratch/verification/mobile.png', full_page=True)

        browser.close()

run()
