import os
from playwright.sync_api import expect
from pages import login_page
from pages.login_page import LoginPage


def test_login(custom_page):
    login_page = LoginPage(custom_page)

    login_page.open_application()
    login_page.login("hashedintestuser109", "Hashedintestuser109@12345")
    #wait for 5 seconds for the dashboard to load
    custom_page.wait_for_timeout(8000)
    login_page.close_popup_if_visible()
    #login_page.validate_dashboard_visible()
    #Dashboard should be visible after successful login
    custom_page.wait_for_timeout(5000)
    expect(login_page.dashboard_heading).to_be_visible(timeout=10000)
    expect(login_page.demand_Pursuits).to_be_visible(timeout=10000)
    print ("Login successful and dashboard is visible.")
    custom_page.close()