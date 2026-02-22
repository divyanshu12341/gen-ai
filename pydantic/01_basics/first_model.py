# All pydantic models inherit from base models 
# 
print("Start of pydantic journey")
from pydantic import BaseModel 
class User(BaseModel):
    id:int
    name:str
    is_active:bool

input_data = {
    'id':101,
    'name':"Divyanshu",
    'is_active':True
}
# here we use ** to unpack dictionary
user = User(**input_data)
print(user)
