import os
from playwright.sync_api import expect
from pages import login_page
from pages.login_page import LoginPage
from pages.Dashboard_Validation_page import DashboardPage
from pages.Logout_page import LogoutPage

def test_logout(login):
     page = login
     dashboard_page = DashboardPage(page)
     logout_page = LogoutPage(page)
     logout_page.perform_logout()
     expect(logout_page.lbl_login_to_continue).to_be_visible(timeout=10000)
