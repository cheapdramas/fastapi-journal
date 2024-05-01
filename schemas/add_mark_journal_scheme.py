from pydantic import BaseModel

class AddMarkScheme(BaseModel):
    student: str
    subject: str
    mark: int
    reason: str|None = None