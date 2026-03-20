from Functions.Third_Page_Draft_Functions import ThirdPageDraftFunctions
from Data.Draft_Data import DraftPageMother


class ThirdPageDraftProcesses:

    def __init__(self, draft: ThirdPageDraftFunctions):     
        self.draft = draft


    def run_third_draft(self):
        test_data = DraftPageMother().get()

        self.draft.academic_year(test_data.DraftData.academic_year)
        self.draft.initial_option()
        self.draft.secondary_option()
        self.draft.from_date()
        self.draft.until_date()
        # self.draft.initial_bed()
        self.draft.secondary_bed()
        self.draft.contin()
        self.draft.back()
