from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Objects.Dashboard_Status_Objects import DashboardStatusObjects
import time 

class DashboardFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.dashboard = DashboardStatusObjects


    def verify_draft(self):
        self.wait.until(EC.element_to_be_clickable(self.dashboard.show_draft_on)).click()
        time.sleep(3)
        text = self.wait.until(EC.visibility_of_element_located(self.dashboard.status)).text.strip()
        print("Currrent Status : ",text)
        

    def verify_status(self):
        text = self.wait.until(EC.visibility_of_element_located(self.dashboard.status)).text.strip()
        print("Currrent Status : ",text)


    









        