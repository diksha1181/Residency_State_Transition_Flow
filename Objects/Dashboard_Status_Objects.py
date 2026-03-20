from selenium.webdriver.common.by import By

class DashboardStatusObjects:

    show_draft_on =(By.CSS_SELECTOR,"[data-test-id='switch-show-draft']")  
    status = (By.CSS_SELECTOR, "[data-test-id='chip-status-desktop-stay-application-0']")
