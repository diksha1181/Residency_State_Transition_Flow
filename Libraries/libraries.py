import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Import_libraries:

    By = By
    WebDriverWait = WebDriverWait

    _driver = None
    keep_browser_open = False

    @classmethod
    def get_driver(cls, browser='chrome'):
        if cls._driver is None:

            remote_url = os.environ.get("SELENIUM_REMOTE_URL")
            headless = os.environ.get("SELENIUM_HEADLESS", "0") == "1"

            if browser.lower() == 'firefox':
                options = FirefoxOptions()
                
                if headless:
                    options.add_argument("--headless")
                    print("Running Firefox in headless mode")

                options.add_argument("--width=1920")
                options.add_argument("--height=1080")

                if remote_url:
                    print(f"Using remote Selenium server at {remote_url}")
                    cls._driver = webdriver.Remote(
                        command_executor=remote_url,
                        options=options
                    )
                else:
                    print("Using local Firefox driver")
                    try:
                        service = FirefoxService(GeckoDriverManager().install())
                    except ValueError as e:
                        if "API rate limit exceeded" in str(e):
                            print("GitHub rate limit hit. Check PATH for geckodriver or wait.")
                            service = FirefoxService()
                        else:
                            raise
                    cls._driver = webdriver.Firefox(
                        service=service,
                        options=options
                    )
            else:
                options = ChromeOptions()

                if headless:
                    options.add_argument("--headless=new")
                    print("Running in headless mode")

                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")

                if remote_url:
                    print(f"Using remote Selenium server at {remote_url}")
                    cls._driver = webdriver.Remote(
                        command_executor=remote_url,
                        options=options
                    )
                else:
                    print("Using local Chrome driver")
                    try:
                        service = Service(ChromeDriverManager().install())
                    except ValueError as e:
                        if "API rate limit exceeded" in str(e):
                            print("GitHub rate limit hit. Check PATH for chromedriver or wait.")
                            service = Service()
                        else:
                            raise
                    cls._driver = webdriver.Chrome(
                        service=service,
                        options=options
                    )

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
