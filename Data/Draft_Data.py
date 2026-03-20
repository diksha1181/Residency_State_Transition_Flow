import os
import dotenv
from faker import Faker
from Model.Draft_Model import DraftData, DraftModel

class DraftPageMother:
    def __init__(self):
        self.fake = Faker()
        dotenv.load_dotenv()
        self.id_number = self.fake.random_number(digits=9, fix_len=True)
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.telephone_number = "6" + str(self.fake.random_number(digits=8, fix_len=True))
        self.email = self.fake.email()
        self.GFN = self.fake.first_name()
        self.GLN = self.fake.last_name()
        self.GM = self.fake.email()
        self.academic_year = self.fake.random_number(digits=4, fix_len=True)

    def get(self) -> DraftModel:
        return DraftModel(
            DraftData = DraftData(
                id_number=self.id_number,
                first_name=self.first_name,
                last_name=self.last_name,
                telephone_number=self.telephone_number,
                email=self.email,
                GFN=self.GFN,
                GLN=self.GLN,
                GM=self.GM,
                academic_year=self.academic_year
            )
        )

