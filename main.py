from Data.Config_Data import ConfigData
from Libraries.libraries import Import_libraries
from Functions.Login_Functions import LoginFunctions
from Functions.First_Page_Draft_Functions import FirstPageDraftFunctions
from Functions.Second_Page_Draft_Functions import SecondPageDraftFunctions
from Functions.Third_Page_Draft_Functions import ThirdPageDraftFunctions
from Functions.Dashboard_Functions import DashboardFunctions
from Functions.State_Change_Functions import StateChangeFunctions





from Processes.Login_Processes import LoginProcesses
from Processes.First_Page_Draft_Processes import FirstPageDraftProcesses
from Processes.Second_Page_Draft_Processes import SecondPageDraftProcesses
from Processes.Third_Page_Draft_Processes import ThirdPageDraftProcesses
from Processes.Dashboard_Processes import DashboardProcesses
from Processes.State_Change_Processes import StateChangeProcesses




data = ConfigData()
driver = Import_libraries.get_driver('firefox')



login_functions = LoginFunctions(driver)
first_page_draft_functions = FirstPageDraftFunctions(driver)
second_page_draft_functions = SecondPageDraftFunctions(driver)
third_page_draft_functions = ThirdPageDraftFunctions(driver)
dashboard_functions = DashboardFunctions(driver)
StateChangefxn = StateChangeFunctions(driver)





login_process = LoginProcesses(login_functions)
first_page_draft_process = FirstPageDraftProcesses(first_page_draft_functions)
second_page_draft_process = SecondPageDraftProcesses(second_page_draft_functions)
third_page_draft_process = ThirdPageDraftProcesses(third_page_draft_functions)
dashboard_processes = DashboardProcesses(dashboard_functions)
StateChange_processes = StateChangeProcesses(StateChangefxn, dashboard_functions)




def test_login():
    login_process.run_login(data.LOGIN_URL, data.EMAIL, data.PASSWORD)

def test_first_page_draft():
    first_page_draft_process.run_first_draft()


def test_second_page_draft():
    second_page_draft_process.run_second_draft()

def test_third_page_draft():
    third_page_draft_process.run_third_draft()    

def test_dashboard():
    dashboard_processes.run_dash()

def test_draft_to_Ip():
    StateChange_processes.run_state()


    

    


def test_driver_close():
    driver.close()



