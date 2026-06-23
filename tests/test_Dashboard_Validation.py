import re
from playwright.sync_api import expect
from pages import login_page
from pages.login_page import LoginPage
from pages.Dashboard_Validation_page import DashboardPage

def test_Categories_Validation(login):
    page = login
    dashboard_page = DashboardPage(page)
    expect(dashboard_page.lbl_All_Categories).to_be_visible(timeout=10000)
    expect(dashboard_page.lbl_New_Categories).to_be_visible(timeout=10000)
    expect(dashboard_page.lbl_In_Progress_Categories).to_be_visible(timeout=10000)
    expect(dashboard_page.lbl_Cancelled_Categories).to_be_visible(timeout=10000)
    expect(dashboard_page.lbl_Won_Categories).to_be_visible(timeout=10000)
    #scroll left to right to make the Deferred category visible and validate its visibility
    page.mouse.wheel(1000, 100)
    expect(dashboard_page.lbl_Deferred_Categories).to_be_visible(timeout=10000)
    print("All categories are visible on the dashboard.")
    page.close()

def test_dashboard_validation(login):
    page = login
    dashboard = DashboardPage(page)
    print("===== Dashboard Validation Started =====")
    dashboard.validate_dashboard_categories()
    expect(dashboard.lbl_All_Categories).to_be_visible(timeout=10000)
    dashboard.validate_list_of_pursuits()
    expect(dashboard.list_Pursuits).to_be_visible(timeout=10000)
    dashboard.validate_left_menu()
    expect(dashboard.mnu_Collapse).to_be_visible()
    expect(dashboard.mnu_Demand_Pursuits).to_be_visible()
    expect(dashboard.mnu_Create_Pursuit).to_be_visible()
    print("Left Menu validated successfully")
    print("===== Dashboard Validation Completed =====")
    