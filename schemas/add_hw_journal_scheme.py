from pydantic import BaseModel



class AddHwJournalScheme(BaseModel):
    date:str
    subject:str
    homework: str