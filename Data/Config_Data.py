import dotenv
import os

class ConfigData:
    def __init__(self):
        dotenv.load_dotenv()
      
        self.LOGIN_URL = os.getenv("LOGIN_URL")
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")
        self.TIMEOUT = int(os.getenv("TIMEOUT")) if os.getenv("TIMEOUT") else None
