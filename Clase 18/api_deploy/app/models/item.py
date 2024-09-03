from pydantic import BaseModel

class InputData(BaseModel):
    jobtitle: str
    age: float
    performance: float
    education: str
    department: str
    seniority: float
    gender: str
