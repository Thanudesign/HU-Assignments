import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.Dashboard_Validation_page import DashboardPage


class LogoutPage:
    def __init__(self, page: Page):
        
        self.page = page
        self.btn_profile_button =page.locator("//div[@class='user-profile-trigger false']")
        self.btn_logout_button =page.locator("//body//div//a[4]")
        self.lbl_login_to_continue=page.locator("//h1[normalize-space()='Login to continue']")



    def perform_logout(self):
        self.btn_profile_button.click()
        self.btn_logout_button.click()
        