# Browser Functionality 

import json
from pathlib import Path
from playwright.sync_api import sync_playwright

# Load Environement Variables
def _load_env():
    config_path = Path(__file__).resolve().parent.parent / "config" / "environemnt.json"
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)

# Launch Browser
def launch_browser():
    env = _load_env()

    playwright = sync_playwright().start()

    if env["browser"] == "chrome":
        browser = playwright.chromium.launch(
            channel="chrome",
            headless=env["headless"],
        )
        print("Chrome Browser is Successfully Launched")
    else:
        browser = getattr(playwright, env["browser"]).launch(
            headless=env["headless"],
        )

    return browser

# Maximize Browser
def maximize_browser(page):
    browser = page.context.browser
    if browser.browser_type.name == "chromium":
        session = page.context.new_cdp_session(page)
        window_id = session.send("Browser.getWindowForTarget")["windowId"]
        session.send(
            "Browser.setWindowBounds",
            {"windowId": window_id, "bounds": {"windowState": "maximized"}},
        )
        print("Browser is been maximised")
    else:
        screen = page.evaluate(
            "({width: window.screen.availWidth, height: window.screen.availHeight})"
        )
        page.set_viewport_size(screen)

# Check if Page is Loaded
def is_page_loaded(page):
    return page.evaluate("document.readyState") == "complete"
    print("Page reload is complete")

# Close Browser
def close_browser(browser):
    browser.close()
    print("Browser closed")
