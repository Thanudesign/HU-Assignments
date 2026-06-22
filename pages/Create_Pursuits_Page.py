import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.Dashboard_Validation_page import DashboardPage
import random 
from faker import Faker


class CreatePursuitsPage:
    def __init__(self, page: Page):
        
        self.page = page
        self.btn_Create_Pursuit = page.locator("[class='_menuItemIcon_1tt27_90']").nth(2)
        self.lbl_Create_Pursuit_Page = page.locator("//span[normalize-space()='Create Pursuit']")
        self.lbl_Pursuit_Details= page.get_by_text("Pursuit Details")


        self.lbl_Add_New_Client = page.locator("//span[normalize-space()='Add New Client']")
        self.lbl_Client = page.get_by_text("Client").nth(1)
        self.lbl_Pursuit_Name = page.get_by_text("Pursuit Name").nth(0)
        self.lbl_Proposal_Type= page.get_by_text("Proposal Type").nth(0)
        self.lbl_Type_Of_Project= page.get_by_text("Type Of Project").nth(0)
        self.lbl_Country= page.get_by_text("Country").nth(0)
        self.lbl_Industry= page.get_by_text("Industry").nth(0)
        self.lbl_Sector= page.get_by_text("Sector").nth(0)
        self.lbl_Billing_Arrangement= page.get_by_text("Billing Arrangement").nth(0)
        self.lbl_Creator= page.get_by_text("Creator")
        self.lbl_Project_Duration= page.get_by_text("Project Duration")
        self.lbl_Jupitor_ID= page.get_by_text("Jupiter ID").nth(0)
        self.lbl_Utilization_AI_Assist= page.get_by_text("Utilizing AI Assist")
        self.lbl_Description= page.locator("//span[contains(text(),'Description')]")
        self.lbl_Reference_Links_to_Shared_Drive= page.get_by_text("Reference / Links to Shared Drive")
        self.btn_Create = self.page.locator("//span[normalize-space()='Create']")
        self.btn_Cancel = self.page.locator("//span[normalize-space()='Cancel']") 

        self.lbl_Client_Name_Required = page.locator("//div[contains(text(),'Client name is required')]")
        self.lbl_Pursuit_Name_Required = page.locator("//span[normalize-space()='Pursuit name is required']")
        self.lbl_Proposal_Type_Required = page.locator("//div[contains(text(),'Proposal type is required')]")
        self.lbl_Type_Of_Project_Required = page.locator("//div[contains(text(),'Project type is required')]")
        self.lbl_Country_Required = page.locator("//div[contains(text(),'Country is required')]")
        self.lbl_Industry_Required = page.locator("//div[contains(text(),'Industry is required')]")
        self.lbl_Sector_Required = page.locator("//div[contains(text(),'Sector is required')]")
        self.lbl_Billing_Arrangement_Required = page.locator("//div[contains(text(),'Billing arrangement is required')]")
        # self.lbl_Creator_Required = page.locator("//div[contains(text(),'Creator is required')]")
        self.lbl_Project_Duration_Required = page.locator("//div[contains(text(),'Date range is required')]")

        self.lbl_Client_Details = page.locator("//div[@class='dna-modal-title']")
        self.lbl_Client_Add_new= page.get_by_text('Client').nth(4)
        self.lbl_Industry_Add_new= page.get_by_text("Industry").nth(2)
        self.lbl_Sector_Add_new= page.get_by_text("Sector").nth(1)
        self.lbl_Save = page.locator("//span[normalize-space()='Save']")
        self.lbl_Cancel = page.locator("//span[normalize-space()='Cancel']").nth(1)

        self.txt_client =page.locator("//input[@placeholder='Add New Client']")
        self.dd_Industry=page.locator('#rc_select_14')
        self.dd_sector=page.locator('#rc_select_15')

        self.opt_Industry=page.get_by_text('Technology Media and Telecom').nth(0)
        self.opt_Sector=page.get_by_text('Telecom, Media and Entertainment').nth(1)

        # Locate the pursuit name textbox by its placeholder
        self.txt_Pursuits = page.locator("input[placeholder='Enter pursuit name']")

        self.dd_Proposal_Type =page.locator("//span[contains(text(),'Select proposal type')]")
        self.opt_Proposal_Type =page.get_by_role("option", name="RFI",exact=True)

        self.dd_Type_Of_Project=page.locator("//span[contains(text(),'Select project type')]")
        self.opt_Type_of_Project=page.get_by_role("option", name="Test Automation",exact=True)

        self.dd_Country=page.locator("#rc_select_10")
        self.opt_Country=page.get_by_title('India')

        self.dd_Billing_arrangement=page.locator("#rc_select_13")
        self.opt_Billing_arrangement=page.get_by_role("Fixed Fee", exact=True)

        self.txt_Jupitet_ID=page.get_by_placeholder("Enter jupiter ID")

        self.date_range=page.locator(".ant-picker-range")

        self.lbl_Success_Message=page.get_by_text("Successfully submitted")
        self.lbl_Pursuit_created=page.get_by_text("New pursuit is created")

        self.txt_Search=page.locator('[placeholder="Search Client, Pursuit, JupiterID"]')
        self.btn_Search=page.locator(".pursuit-search-button")
        #self.lbl_Searched_Result=page.get_by_text(f"text= {pursuit_name}")
        self.row_first_result = page.locator("tbody tr td").first

        self.lbl_pursuit_ID=page.get_by_text("Pursuit ID")
        self.lbl_Proposal_Type=page.get_by_text("Proposal Type")
        self.lbl_Edit=page.locator("(//button[@type='button'])[5]")
        self.lbl_View_More=page.locator("(//button[@type='button'])[6]")
        
        
        # Required Fields
    def click_Create_Pursuit(self):
        self.btn_Create_Pursuit.click(force=True)
        print("Clicked on Create Pursuit button")

    def validate_Create_Pursuit_Page(self):
        expect(self.lbl_Create_Pursuit_Page).to_be_visible(timeout=10000)
        print("Create Pursuit page is displayed")
    def validate_required_fields_error(self):
        self.btn_Create.click()
        print("Clicked on Create button without filling required fields to validate error messages")
    def Add_New_Client(self):
        self.lbl_Add_New_Client.click(force=True)
        print("Clicked on Add New Client button to add a new client")
        self.page.wait_for_timeout(2000)
    def click_Create(self):
        self.btn_Create.click()
        print("Clicked on Create button to create a new pursuit")

    def create_client(self):
        fake = Faker()
        client_name = f"{fake.first_name()}{random.randint(1000,9999)}"
        self.txt_client.fill(client_name)
        self.dd_Industry.click(force=True)
        self.opt_Industry.click()
        self.dd_sector.click(force=True)
        self.page.wait_for_timeout(2000)
        self.opt_Sector.click()
        self.page.wait_for_timeout(4000)
        self.lbl_Save.click()

        #self.txt_Pursuits.fill('beta')
        self.pursuit_name=f"beta{random.randint(1000,9999)}"
        self.txt_Pursuits.fill(self.pursuit_name)
        print(self.page.locator("//span[contains(text(),'Select proposal type')]").count())
        self.dd_Proposal_Type.click(force=True)
        self.page.locator("#rc_select_8").fill("RFI")
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        print(self.page.locator("//span[contains(text(),'Select project type')]").count())
        self.dd_Type_Of_Project.click(force=True)
        self.page.locator("#rc_select_9").fill("Test Automation")
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        print(self.page.locator("//span[contains(text(),'Select country')]").count())
        self.dd_Country.click(force=True)
        self.dd_Country.fill('India')
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        print(self.page.locator("//span[contains(text(),'Select country')]").count())
        self.dd_Billing_arrangement.click(force=True)
        self.dd_Billing_arrangement.fill("Fixed Fee")
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.txt_Jupitet_ID.fill("JUPI123456")

        self.page.locator(".ant-picker-range").click()
        # collect enabled date cells and select a start and end date
        dates = self.page.locator(".ant-picker-cell:not(.ant-picker-cell-disabled)")
        dates.nth(0).click()
        dates.nth(5).click()
        self.page.get_by_role("button", name="Done").click()
        print("Project duration selected successfully")
        self.txt_Pursuits.fill(self.pursuit_name)
        print(f"Pursuit Name Created : {self.pursuit_name}")
        return self.pursuit_name
    
    def search_pursuit(self, pursuit_name):
        self.btn_Search.click()
        self.txt_Search.wait_for(state="visible")
        self.txt_Search.click(force=True)
        self.txt_Search.fill(pursuit_name)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(3000)

    def click_searched_pursuit(self):
         self.row_first_result.click(force=True)

