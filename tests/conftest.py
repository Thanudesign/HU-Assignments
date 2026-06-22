import pytest
from playwright.sync_api import sync_playwright
import os

# Create the screenshots directory if it doesn't exist
os.makedirs("screenshots", exist_ok=True)
os.makedirs("videos", exist_ok=True)

@pytest.fixture(scope="function")
def custom_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        record_video_path = "videos/test_video.mp4"
        context = browser.new_context(record_video_dir="videos")
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # Access the page fixture
        custom_page = item.funcargs['custom_page']
        # Save a screenshot on failure
        screenshot_path = f"screenshots/{item.name}.png"
        custom_page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

@pytest.fixture
def login(custom_page):
    from pages.login_page import LoginPage
    login_page = LoginPage(custom_page)
    login_page.open_application()
    login_page.login("hashedintestuser109", "Hashedintestuser109@12345")
    custom_page.wait_for_timeout(10000)
    login_page.close_popup_if_visible()
    custom_page.wait_for_timeout(7000)
    return custom_page
            