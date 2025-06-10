from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    email: EmailStr
    password: str
    role: Literal["student", "teacher", "parent"]

    college: Optional[str] = None         # For student
    roll_number: Optional[str] = Field(None, alias="rollNumber")  # For student
    department: Optional[str] = None      # For teacher
    subjects: Optional[str] = None        # For teacher
    child_name: Optional[str] = Field(None, alias="childName")    # For parent
    relation: Optional[str] = None        # For parent

    class Config:
        allow_population_by_field_name = True

class UserOut(BaseModel):
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    email: EmailStr
    role: str
    token: str

    class Config:
        allow_population_by_field_name = True
        by_alias = True

class TokenResponse(BaseModel):
    token: str
    role: str
    token_type: str = "bearer"
