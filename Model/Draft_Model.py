from pydantic import BaseModel

class DraftData(BaseModel):
    id_number: int
    first_name: str
    last_name: str
    telephone_number: str
    email: str
    GFN: str
    GLN: str
    GM: str
    academic_year: int

class DraftModel(BaseModel):
    DraftData: DraftData
