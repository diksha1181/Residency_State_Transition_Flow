from Functions.Second_Page_Draft_Functions import SecondPageDraftFunctions
from Data.Draft_Data import DraftPageMother


class SecondPageDraftProcesses:

    def __init__(self, draft: SecondPageDraftFunctions):     
        self.draft = draft


    def run_second_draft(self):
        test_data = DraftPageMother().get()

        self.draft.grade()
        self.draft.year()
        self.draft.semester()
        self.draft.upload_PO_residence_document()
        self.draft.schtype()
        self.draft.schapplication()
        self.draft.Guardian(test_data.DraftData.GFN, test_data.DraftData.GLN, test_data.DraftData.GM, test_data.DraftData.telephone_number)
        self.draft.contin()
