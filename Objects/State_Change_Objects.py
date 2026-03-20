from selenium.webdriver.common.by import By

class StateChangeObjects:
        
    edit = (By.CSS_SELECTOR,"[data-test-id='icon-btn-edit-stay-application-0']")   
    conti = (By.CSS_SELECTOR,"[data-test-id='text-next-desktop-navigation-footer']")
    accomodation = (By.CSS_SELECTOR,"[data-test-id='tab-desktop-stay-application-request-contract']")
    click_bed = (By.XPATH,"//h6[normalize-space()='BED-SS-002-B']")
    waiting = (By.CSS_SELECTOR,"[data-test-id='btn-move-application-to-waiting-list']")
    confirm_wait = (By.CSS_SELECTOR,"[data-test-id='btn-confirm-move-application-to-waiting-list-dialog']")
    inprocess = (By.CSS_SELECTOR,"[data-test-id='btn-move-application-to-in-process']")
    confirm_ip = (By.CSS_SELECTOR,"[data-test-id='btn-confirm-move-application-to-in-process-dialog']")
    pre_reserve = (By.CSS_SELECTOR,"[data-test-id='btn-pre-reserve-stay-application']")
    confirm_pre = (By.CSS_SELECTOR,"[data-test-id='btn-confirm-pre-reserve-application-dialog']")
   
    


    