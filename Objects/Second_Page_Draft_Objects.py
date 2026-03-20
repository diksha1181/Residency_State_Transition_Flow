from selenium.webdriver.common.by import By

class SecondPageDraftObjects:
    
    grade = (By.XPATH,"//div[@id='mui-component-select-grade']")
    year = (By.XPATH,"//div[@id='mui-component-select-academic_year']")
    semester = (By.XPATH,"//div[@id='mui-component-select-semester']")
    upload_image = By.CSS_SELECTOR, "input[type='file']"  
    SchType = (By.XPATH,"//div[@id='mui-component-select-scholarship_type']")
    SchApplication = (By.CSS_SELECTOR,"[data-test-id='text-input-scholarship-application-academic-details']")
    Guardian_First = (By.XPATH,"//span[normalize-space()='Father']")
    Guardian_FN = (By.CSS_SELECTOR,"[data-test-id='input-0-first-name-tutor-details']")
    Guardian_LN = (By.CSS_SELECTOR,"[data-test-id='input-0-last-name-tutor-details']")
    Guardian_email = (By.CSS_SELECTOR,"[data-test-id='input-0-email-tutor-details']")
    Guardian_no = (By.CSS_SELECTOR,"input[data-test-id='input-0-telephone-tutor-details']")
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='text-next-desktop-navigation-footer']")
