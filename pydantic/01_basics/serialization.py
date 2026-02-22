from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool = True
    createdat:datetime
    address:Address
    tags:List[str] = []
    model_config = ConfigDict(
        json_encoders = {datetime:lambda v:v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name='Divyanshu',
    email = "divyanshu@123ai",
    createdat = datetime(2024,3,15,14,30,12),
    address = Address(
        street = "Something",
        city = "Jaipur",
        zip_code ="009987",
    ),
    is_active = True,
    tags = ['premium','sub']
)

# way to convert model into dictionary 
python_dict = user.model_dump()
print(python_dict)

# way to convert model into string 
json_str = user.model_dump_json()
print(json_str)
