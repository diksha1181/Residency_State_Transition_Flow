from selenium.webdriver.common.by import By

class LoginObjects:
    Language_Dropdown = (By.CSS_SELECTOR, "[data-test-id='icon-language-selector-arrow-drop-down']")
    Language_Option_EN = (By.CSS_SELECTOR, "[data-test-id='text-en-US-language']")
    
    Google_Login_Button = (By.XPATH, "//button[contains(.,'Google')]")
    Email_Input = (By.ID, "identifierId")
    Email_Next = (By.ID, "identifierNext")
    Password_Input = (By.NAME, "Passwd")
    Password_Next = (By.ID, "passwordNext")
    Login_Success_Element = (By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-titleLg.css-152msal")    
    Home_Menu = (By.CSS_SELECTOR, "[data-test-id='text-profile-name']")
