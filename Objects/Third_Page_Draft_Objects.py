from selenium.webdriver.common.by import By

class ThirdPageDraftObjects:
    
    academic_year = (By.CSS_SELECTOR,"[data-test-id='input-course-accommodation-course-stay-contract-form']")
    initial_option = (By.CSS_SELECTOR,"[data-test-id='select-display-initial-option-type-of-accommodation-stay-contract-form']")
    secondary_option = (By.CSS_SELECTOR,"[data-test-id='select-display-second-option-type-of-accommodation-stay-contract-form']")
    from_date = (By.CSS_SELECTOR,"[data-test-id='btn-date-picker-open-from-date-accommodation-dates-and-guest-type-stay-contract-form']")
    Date_Select = (By.XPATH, "//button[normalize-space()='Select']")
    until_date = (By.CSS_SELECTOR,"[data-test-id='btn-date-picker-open-until-date-accommodation-dates-and-guest-type-stay-contract-form']")
    initial_bed = (By.XPATH,"//h6[normalize-space()='BED-IS-002-A']")
    secondary_bed = (By.XPATH,"//h6[normalize-space()='BED-SS-002-A']")
    continue_btn = (By.CSS_SELECTOR,"[data-test-id='text-next-desktop-navigation-footer']")
 





