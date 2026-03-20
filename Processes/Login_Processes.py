from Functions.Login_Functions import LoginFunctions

class LoginProcesses:

    def __init__(self, login: LoginFunctions):     
        self.login = login

    def run_login(self, url, email, password):
        main_window = self.login.open_application(url)

        self.login.select_language()

        self.login.click_google_login()

        self.login.switch_to_popup_window(main_window)

        self.login.enter_email(email)

        self.login.enter_password(password)

        self.login.verify_login_success()

        