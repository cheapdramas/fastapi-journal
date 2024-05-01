from pydantic import BaseModel


class Check_device(BaseModel):
    device: str

class Add_device(BaseModel):
    device: str
    id: int