from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from Objects.State_Change_Objects import StateChangeObjects

class StateChangeFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.state = StateChangeObjects


    def Draft_To_Ip(self):
        self.wait.until(EC.element_to_be_clickable(self.state.edit)).click()
        time.sleep(5)
        for _ in range(4):
            elem = self.wait.until(EC.element_to_be_clickable(self.state.conti))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            self.driver.execute_script("arguments[0].click();", elem)
            time.sleep(2)
        time.sleep(3)


    def IP_To_Wait(self):
        self.wait.until(EC.element_to_be_clickable(self.state.edit)).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.state.accomodation)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.state.click_bed)).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.state.waiting)).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.state.confirm_wait)).click()
        time.sleep(5)


    def Wait_To_IP(self):

        self.wait.until(EC.element_to_be_clickable(self.state.edit)).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.state.accomodation)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.state.click_bed)).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.state.inprocess)).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.state.confirm_ip)).click()
        time.sleep(5)



    def IP_To_Pre(self):

        self.wait.until(EC.element_to_be_clickable(self.state.edit)).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.state.pre_reserve)).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.state.confirm_pre)).click()
        time.sleep(5)


    def back(self):
        self.driver.back()
        time.sleep(2)


        



        
    
        


    


    


    
        

    

    
