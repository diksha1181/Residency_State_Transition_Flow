from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from Objects.Third_Page_Draft_Objects import ThirdPageDraftObjects
import time


class ThirdPageDraftFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.Draft = ThirdPageDraftObjects



    def academic_year(self, academic_year):
       self.driver.find_element(*self.Draft.academic_year).send_keys(academic_year)
       time.sleep(2)

    def initial_option(self):
        elem_11 = self.wait.until(EC.element_to_be_clickable(self.Draft.initial_option))
        elem_11.click()
        time.sleep(2)
        initial_option_choice = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-test-id='li-initial-option-type-of-accommodation-stay-contract-form-individualStudio']"))
        )
        initial_option_choice.click()
        time.sleep(2)

    def secondary_option(self):
        elem_12 = self.wait.until(EC.element_to_be_clickable(self.Draft.secondary_option))
        elem_12.click()
        time.sleep(2)
        secondary_option_choice = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-test-id='li-second-option-type-of-accommodation-stay-contract-form-sharedStudio']"))
        )
        secondary_option_choice.click()
        time.sleep(2)

    def from_date(self):

        target_date = datetime.strptime('04/01/2026', '%m/%d/%Y')
        target_day = str(target_date.day)

        self.wait.until(
            EC.element_to_be_clickable(self.Draft.from_date)
        ).click()

        while True:
            current_text = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".MuiPickersCalendarHeader-label")
                )
            ).text.strip()

            current_date = datetime.strptime(current_text, "%B %Y")

            if current_date.year == target_date.year and current_date.month == target_date.month:
                break

            elif current_date < target_date:
                next_btn = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@aria-label,'Next')]")
                    )
                )
                self.driver.execute_script("arguments[0].click();", next_btn)

            else:
                prev_btn = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@aria-label,'Previous')]")
                    )
                )
                self.driver.execute_script("arguments[0].click();", prev_btn)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[normalize-space()='{target_day}']")
            )
        ).click()

        
        self.wait.until(EC.element_to_be_clickable((self.Draft.Date_Select))).click()

        time.sleep(2)


    def until_date(self):
        target_date = datetime.strptime('04/30/2026', '%m/%d/%Y')
        target_day = str(target_date.day)

        self.wait.until(
            EC.element_to_be_clickable(self.Draft.until_date)
        ).click()

        while True:
            current_text = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".MuiPickersCalendarHeader-label")
                )
            ).text.strip()

            current_date = datetime.strptime(current_text, "%B %Y")

            if current_date.year == target_date.year and current_date.month == target_date.month:
                break

            elif current_date < target_date:
                next_btn = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@aria-label,'Next')]")
                    )
                )
                self.driver.execute_script("arguments[0].click();", next_btn)

            else:
                prev_btn = self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@aria-label,'Previous')]")
                    )
                )
                self.driver.execute_script("arguments[0].click();", prev_btn)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[normalize-space()='{target_day}']")
            )
        ).click()



        self.wait.until(EC.element_to_be_clickable((self.Draft.Date_Select))).click()

        time.sleep(2)


    def initial_bed(self):
        self.wait.until(EC.element_to_be_clickable(self.Draft.initial_bed)).click()        
        time.sleep(2)

    def secondary_bed(self):
        self.wait.until(EC.element_to_be_clickable(self.Draft.secondary_bed)).click()
        time.sleep(2)

    def contin(self):
        self.wait.until(EC.element_to_be_clickable(self.Draft.continue_btn)).click()
        time.sleep(2)

    def back(self):
        self.driver.back()
        time.sleep(2)

    



