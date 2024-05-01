from pydantic import BaseModel

class AddDeviceScheme(BaseModel):
    device_id : str
    log_id : int|str
    is_teacher : bool = False
