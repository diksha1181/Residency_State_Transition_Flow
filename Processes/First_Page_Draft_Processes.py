from Functions.First_Page_Draft_Functions import FirstPageDraftFunctions
from Data.Draft_Data import DraftPageMother

class FirstPageDraftProcesses:

    def __init__(self,  draft: FirstPageDraftFunctions):     
        self.draft = draft

    def run_first_draft(self):
        test_data = DraftPageMother().get()
        
        self.draft.new_app()
        self.draft.select_type()
        self.draft.select_passport()
        self.draft.enter_id_no(test_data.DraftData.id_number)
        self.draft.enter_first_name(test_data.DraftData.first_name)
        self.draft.enter_last_name(test_data.DraftData.last_name)
        self.draft.gender()
        self.draft.country()
        self.draft.DOB()
        self.draft.telephone(test_data.DraftData.telephone_number)
        self.draft.email(test_data.DraftData.email)
        self.draft.residence()
        self.draft.state()
        self.draft.city()
        self.draft.contin()