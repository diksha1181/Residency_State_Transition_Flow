from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
import time
from Objects.Second_Page_Draft_Objects import SecondPageDraftObjects 


class SecondPageDraftFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.Draft = SecondPageDraftObjects

    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    PO_RESIDENCE_PATH = str(PROJECT_ROOT / "static" / "file-sample_150kB.pdf")


    def grade(self):
        elem_7 = self.wait.until(EC.element_to_be_clickable(self.Draft.grade))
        elem_7.click()
        time.sleep(2)
        grade_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Master in Business Administration and Management']"))
        )
        grade_option.click()
        time.sleep(2)

    def year(self):
        elem_8 = self.wait.until(EC.element_to_be_clickable(self.Draft.year))
        elem_8.click()
        time.sleep(2)
        year_option = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-test-id='li-academic-year-academic-details-2023-2024']"))
        )
        year_option.click()
        time.sleep(2)

    def semester(self):
        elem_9 = self.wait.until(EC.element_to_be_clickable(self.Draft.semester))
        elem_9.click()
        time.sleep(2)
        semester_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Extraordinary']"))
        )
        semester_option.click()
        time.sleep(2)


    def upload_PO_residence_document(self, residence_doc=None):
      try:
        file_path = residence_doc or self.PO_RESIDENCE_PATH
        upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.Draft.upload_image)
        )
        # Send file path to <input type=file>
        upload_input.send_keys(file_path)
        print(f" File uploaded: {file_path}")
        time.sleep(3)
      except Exception as e:
        print(f" Unable to upload file. Error: {e}")

    

    def schtype(self):
        elem_10 = self.wait.until(EC.element_to_be_clickable(self.Draft.SchType))
        elem_10.click()
        time.sleep(2)
        schtype_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Beca de residencia']"))
        )
        schtype_option.click()
        time.sleep(2)
   

    def schapplication(self, identity_doc=None):
     try:
        file_path = self.PO_RESIDENCE_PATH

        # Get all file inputs
        upload_inputs = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.Draft.upload_image)
        )

        # Upload into second input (index 1)
        upload_inputs[1].send_keys(file_path)

        print(f" Second file uploaded: {file_path}")
        time.sleep(3)

     except Exception as e:
        print(f" Unable to upload second file. Error: {e}")  
   



    def Guardian(self,GFN, GLN, GM, telephone_number):

        self.driver.find_element(*self.Draft.Guardian_First).click()
        
        time.sleep(2)                       

       
        self.wait.until(EC.visibility_of_element_located(self.Draft.Guardian_FN)).send_keys(GFN)
        self.wait.until(EC.visibility_of_element_located(self.Draft.Guardian_LN)).send_keys(GLN)
        self.wait.until(EC.visibility_of_element_located(self.Draft.Guardian_email)).send_keys(GM)
        self.wait.until(EC.visibility_of_element_located(self.Draft.Guardian_no)).send_keys(telephone_number)
        time.sleep(2)

    def contin(self):
        self.wait.until(EC.element_to_be_clickable(self.Draft.continue_btn)).click()
        time.sleep(2)



