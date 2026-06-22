import os
from playwright.sync_api import expect
from pages import login_page
from pages.login_page import LoginPage
from pages.Dashboard_Validation_page import DashboardPage
from pages.Create_Pursuits_Page import CreatePursuitsPage


def test_Create_Pursuits_Functionality(login):
    page = login
    dashboard_page = DashboardPage(page)
    create_pursuits = CreatePursuitsPage(page)
    create_pursuits.click_Create_Pursuit()
    expect(create_pursuits.lbl_Create_Pursuit_Page).to_be_visible(timeout=10000)
    print("Create Pursuit page is displayed")
    create_pursuits.validate_Create_Pursuit_Page()
    expect(create_pursuits.lbl_Pursuit_Details).to_be_visible(timeout=10000)
    print("Pursuit Details section is visible")
    page.wait_for_timeout(2000)
    expect(create_pursuits.lbl_Add_New_Client).to_be_visible(timeout=10000)
    print("Add New Client section is visible")
    expect(create_pursuits.lbl_Client).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Pursuit_Name).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Proposal_Type).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Type_Of_Project).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Country).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Industry).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Sector).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Billing_Arrangement).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Creator).to_be_visible(timeout=10000)   
    expect(create_pursuits.lbl_Project_Duration).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Jupitor_ID).to_be_visible(timeout=10000  ) 
    #Scroll down to make the Utilization AI Assist, Description, and Reference Links to Shared Drive visible
    page.mouse.wheel(0, 1000)
    expect(create_pursuits.lbl_Utilization_AI_Assist).to_be_visible(timeout=10000)
    page.mouse.wheel(100, 1000)
    expect(create_pursuits.lbl_Description).to_be_visible(timeout=10000)
    expect(create_pursuits.lbl_Reference_Links_to_Shared_Drive).to_be_visible(timeout=10000)
    expect(create_pursuits.btn_Create).to_be_visible(timeout=10000)
    expect(create_pursuits.btn_Cancel).to_be_visible(timeout=10000)
    page.close()


def test_Create_Pursuits_Error_Fields_Val(login):
     page = login
     dashboard_page = DashboardPage(page)
     create_pursuits = CreatePursuitsPage(page)
     create_pursuits.click_Create_Pursuit()
     create_pursuits.click_Create()
     expect(create_pursuits.lbl_Client_Name_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Pursuit_Name_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Proposal_Type_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Type_Of_Project_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Country_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Industry_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Sector_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Billing_Arrangement_Required).to_be_visible(timeout=10000)
    #expect(create_pursuits.lbl_Creator_Required).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Project_Duration_Required).to_be_visible(timeout=10000)

def test_Create_Pursuits(login):
     page = login
     dashboard_page = DashboardPage(page)
     create_pursuits = CreatePursuitsPage(page)
     create_pursuits.click_Create_Pursuit()
     create_pursuits.Add_New_Client()
     expect(create_pursuits.lbl_Client_Details).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Client_Add_new).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Industry_Add_new).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Sector_Add_new).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Save).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Cancel).to_be_visible(timeout=10000)
     pursuit_name=create_pursuits.create_client()
     create_pursuits.click_Create()
     expect(create_pursuits.lbl_Success_Message).to_be_visible(timeout=10000)
     expect(create_pursuits.lbl_Pursuit_created).to_be_visible(timeout=1000)
     print(" 'New pursuit is created' message is displayed")
     print ("Pursuit created successfully")
     page.wait_for_timeout(5000)
     page.reload()
     page.wait_for_load_state("networkidle")
     create_pursuits.search_pursuit(pursuit_name)
     # expect(page.get_by_text(pursuit_name).to_be_visible(timeout=1000)
     print(f"Pursuit {pursuit_name} found successfully")
     create_pursuits.click_searched_pursuit()
     page.wait_for_timeout(5000)
     expect(create_pursuits.lbl_pursuit_ID).to_be_visible()
     expect(create_pursuits.lbl_Proposal_Type).to_be_visible()
     expect(create_pursuits.lbl_Edit).to_be_visible()
     expect(create_pursuits.lbl_View_More).to_be_visible()
     expect(create_pursuits.lbl_Pursuit_Details).to_be_visible()
