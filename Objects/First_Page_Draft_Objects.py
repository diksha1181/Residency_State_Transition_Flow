from selenium.webdriver.common.by import By

class FirstPageDraftObjects:
        
    Request_btn = (By.XPATH, "//p[normalize-space()='Requests']")
    New_App = (By.XPATH, "//button[normalize-space()='New Application']")    
    Resident = (By.CSS_SELECTOR, "[data-test-id='text-extended-stay-dialog-type-of-stay']")
    Type = (By.XPATH,"//div[@id='mui-component-select-identification_type']")
    passport = (By.XPATH,"//span[normalize-space()='Passport']")
    id_no = (By.NAME,"identification_number")
    id_v = (By.CSS_SELECTOR,"[data-test-id='btn-end-adornment-personal-documentation-identification-number']")
    create = (By.XPATH,"//button[normalize-space()='Create']")
    First = (By.CSS_SELECTOR,"[data-test-id='input-personal-information-first-name']")
    Last = (By.CSS_SELECTOR,"[data-test-id='input-personal-information-last-name']")
    Gender = (By.CSS_SELECTOR,"[data-test-id='select-display-personal-information-gender']")
    Country = (By.CSS_SELECTOR,"[data-test-id='autocomplete-input-personal-information-nationality']")
    DOB = (By.CSS_SELECTOR,"[data-test-id='btn-date-picker-open-personal-information-date-of-birth']")
    DOB_S = (By.XPATH, "//button[normalize-space()='Select']")
    telephone_number = (By.CSS_SELECTOR, "[data-test-id='input-personal-information-telephone-number']")
    Email = (By.NAME,"personal_information.email")
    Residence = (By.CSS_SELECTOR,"[data-test-id='autocomplete-input-personal-information-country-of-residence']")
    state = (By.CSS_SELECTOR,"[data-test-id='autocomplete-input-personal-information-state']")
    city = (By.CSS_SELECTOR,"[data-test-id='autocomplete-input-personal-information-city']")
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='text-next-desktop-navigation-footer']")


    




    