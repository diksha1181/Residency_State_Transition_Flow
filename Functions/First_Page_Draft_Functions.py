from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from Objects.First_Page_Draft_Objects import FirstPageDraftObjects

class FirstPageDraftFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.Draft = FirstPageDraftObjects


    def new_app(self):
        self.wait.until(EC.visibility_of_element_located(self.Draft.Request_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.Draft.New_App)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.Draft.Resident)).click()
        time.sleep(3)
        
    def select_type(self):        
        self.wait.until(EC.element_to_be_clickable(self.Draft.Type)).click()           
        time.sleep(2)      

    def select_passport(self):
        self.wait.until(EC.element_to_be_clickable(self.Draft.passport)).click()
        time.sleep(2)

    def enter_id_no(self, id_number):
        self.driver.find_element(*self.Draft.id_no).send_keys(id_number)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.Draft.id_v)).click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.Draft.create)).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.Draft.First).send_keys(first_name)
        time.sleep(2)

    def enter_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located(self.Draft.Last)).send_keys(last_name)
        time.sleep(2)

    def gender(self):  
        elem_2 = self.wait.until(EC.element_to_be_clickable(self.Draft.Gender))
        elem_2.click()
        time.sleep(2)
        
        male_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Male']"))
        )
        male_option.click()
        time.sleep(2)

    def country(self):
        elem_3 = self.wait.until(EC.element_to_be_clickable(self.Draft.Country))
        elem_3.click()
        time.sleep(2)
        
        albania_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Albania']"))
        )
        albania_option.click()
        time.sleep(2)

    def DOB(self):
        input_element = self.wait.until(EC.element_to_be_clickable(self.Draft.DOB))
        target_date_str = '12/12/2007'
        target_date = datetime.strptime(target_date_str, '%m/%d/%Y')
        target_month_year = target_date.strftime('%B %Y')  
        target_day = str(target_date.day)

        input_element.click()

        while True:
            current_month_year_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiPickersCalendarHeader-label.date-picker_calendarHeaderLabel__QBx_x.css-8633fn")))
            
            current_month_year_text = current_month_year_element.text.strip()

            if current_month_year_text == target_month_year:
                break
            else:         
                PREV_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Previous month']")))
                PREV_button.click()
                time.sleep(0.5)

        day_element = self.wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//button[normalize-space()='{target_day}']")))
        
        day_element.click()
        self.wait.until(EC.element_to_be_clickable((self.Draft.DOB_S))).click()

        time.sleep(2)

    def telephone(self, telephone_number):
        self.wait.until(EC.visibility_of_element_located(self.Draft.telephone_number)).send_keys(telephone_number)
        time.sleep(2)

    def email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.Draft.Email)).send_keys(email)
        time.sleep(2)

    def residence(self):
        elem_4 = self.wait.until(EC.element_to_be_clickable(self.Draft.Residence))
        elem_4.click()
        time.sleep(2)
        albania_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Albania']"))
        )
        albania_option.click()
        time.sleep(2)

    def state(self):
        elem_5 = self.wait.until(EC.element_to_be_clickable(self.Draft.state))
        elem_5.click()
        time.sleep(2)
        albania_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Berat District']"))
        )
        albania_option.click()
        time.sleep(2)

    def city(self):
        elem_6 = self.wait.until(EC.element_to_be_clickable(self.Draft.city))
        elem_6.click()
        time.sleep(2)
        albania_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Berat']"))
        )
        albania_option.click()
        time.sleep(2)

    def contin(self):
        self.wait.until(EC.element_to_be_clickable(self.Draft.continue_btn)).click()
        time.sleep(2)

