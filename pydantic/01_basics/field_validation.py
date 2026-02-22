
from pydantic import BaseModel


class User(BaseModel):
    username:str
    @field_validator(username)
    def username_length(cls,v):
        if(len(v))<4:
            raise ValueError("Username must be atleast 4 characters")
        return v
class SignUpData(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode = 'after')
    def password_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Value does not match")
        return values
