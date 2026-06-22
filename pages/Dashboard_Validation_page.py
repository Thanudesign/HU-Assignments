from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.lbl_All_Categories = page.locator("//span[normalize-space()='All']")
        self.lbl_New_Categories = page.locator("//span[normalize-space()='New']").nth(0)
        self.lbl_In_Progress_Categories = page.locator("//span[normalize-space()='In Progress']").nth(0)
        self.lbl_Cancelled_Categories = page.locator("//span[normalize-space()='Cancelled']").nth(0)
        self.lbl_Won_Categories = page.locator("//span[normalize-space()='Won']").nth(0)
        #Scroll left to right to make the Deferred category visible
        #page.mouse.wheel(1000, 100)
        self.lbl_Deferred_Categories = page.locator("//span[normalize-space()='Deferred']").nth(0)
        # Category Cards
        self.lbl_All_Count = page.locator("//span[normalize-space()='All']/following-sibling::span")
        self.lbl_New_Count = page.locator("//span[normalize-space()='New']/following-sibling::span")
        self.lbl_In_Progress_Count = page.locator("//span[normalize-space()='In Progress']/following-sibling::span")
        self.lbl_Cancelled_Count = page.locator("//span[normalize-space()='Cancelled']/following-sibling::span")
        self.lbl_Won_Count = page.locator("//span[normalize-space()='Won']/following-sibling::span")
        self.lbl_Deferred_Count = page.locator("//span[normalize-space()='Deferred']/following-sibling::span")

        # List of Pursuits
        self.list_Pursuits = page.locator("//h3[normalize-space()='List of all Pursuits']")

        # Left Navigation
        #self.btn_LeftMenu = page.locator('aria-label="Expand menu"')   # Update XPath if needed
        self.mnu_Collapse = page.locator('[class="_menuItemIcon_1tt27_90"]').nth(0)
        self.mnu_Demand_Pursuits = page.locator('[class="_menuItemIcon_1tt27_90"]').nth(1)
        self.mnu_Create_Pursuit = page.locator("[class='_menuItemIcon_1tt27_90']").nth(2)
    def validate_dashboard_categories(self):
        categories = [
            ("All", self.lbl_All_Count),
            ("New", self.lbl_New_Count),
            ("In Progress", self.lbl_In_Progress_Count),
            ("Cancelled", self.lbl_Cancelled_Count),
            ("Won", self.lbl_Won_Count),
            ("Deferred", self.lbl_Deferred_Count),
        ]
        for category, locator in categories:
            if category == "Deferred":
                # Scroll to make Deferred visible
                #self.page.mouse.wheel(1000, 100)
                self.lbl_Deferred_Count.scroll_into_view_if_needed()
                expect(self.lbl_Deferred_Count).to_be_visible(timeout=10000)
                self.page.wait_for_timeout(1000)
            expect(locator).to_be_visible(timeout=10000)
            count = locator.inner_text()
            print(f"{category} : {count}")
    def validate_list_of_pursuits(self):
        expect(self.list_Pursuits).to_be_visible(timeout=10000)
        print("List of Pursuits is displayed")
    def validate_left_menu(self):
        #self.btn_LeftMenu.click()
        self.mnu_Collapse.click(force=True)
        


