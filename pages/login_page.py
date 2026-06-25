from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.get_by_role("button", name="Login using SSO")
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="submit")
        self.close_button = page.locator('[id="onetrust-close-btn-container"]')
        self.dashboard_heading = page.locator('[class="page-header-container"]')
        self.demand_Pursuits = page.locator("//h2[normalize-space()='Demand Pursuits']")

    def open_application(self):
        self.page.goto("https://dna-preprod.hashedin.com/pursuits")

    def login(self, username: str, password: str):
        self.sign_in_button.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def close_popup_if_visible(self):
        if self.close_button.is_visible(timeout=4000):
            self.close_button.click(force=True)

    def validate_dashboard_visible(self):
        expect(self.dashboard_heading).to_be_visible()