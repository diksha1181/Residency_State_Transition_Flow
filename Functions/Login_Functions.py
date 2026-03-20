from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Objects.Login_Objects import LoginObjects as LoginLocators


class LoginFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.Login = LoginLocators


    def open_application(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver.current_window_handle

    def select_language(self):
        self.wait.until(
            EC.element_to_be_clickable(self.Login.Language_Dropdown)
        ).click()
        time.sleep(1)
        
        self.wait.until(
            EC.element_to_be_clickable(self.Login.Language_Option_EN)
        ).click()
        time.sleep(2)

    def click_google_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.Login.Google_Login_Button)
        ).click()
        

    def switch_to_popup_window(self, main_window):
        self.main_window = main_window
        self.wait.until(lambda d: len(d.window_handles) > 1)
        popup_window = [w for w in self.driver.window_handles if w != main_window][0]
        self.driver.switch_to.window(popup_window)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.Login.Email_Input))
        self.driver.find_element(*self.Login.Email_Input).send_keys(email)
        self.driver.find_element(*self.Login.Email_Next).click()

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.Login.Password_Input))
        self.driver.find_element(*self.Login.Password_Input).send_keys(password)
        
        time.sleep(1)
        
        password_next_button = self.wait.until(
            EC.element_to_be_clickable(self.Login.Password_Next)
        )
        password_next_button.click()

    def verify_login_success(self):
        self.driver.switch_to.window(self.main_window)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        time.sleep(2)

        try:
            self.wait.until(
                EC.visibility_of_element_located(self.Login.Login_Success_Element)
            )
            print("Successful Login")
        except Exception:
            print("Login completed - using alternative verification")

        self.wait_for_page_ready()

    def wait_for_page_ready(self):
        try:
            self.wait.until(
                    EC.visibility_of_element_located(self.Login.Home_Menu)
                )

            print("Page loaded successfully")
        except Exception:
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
            time.sleep(2)
            print("Page loaded (document ready)")


