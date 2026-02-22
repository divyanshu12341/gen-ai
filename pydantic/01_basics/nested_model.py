from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address: Address

address = Address(
    street = "123 Something",
    city = "Jaipur",
    postal_code = "10001"
)
user = User(
    id = 1,
    name = "Divyanshu",
    address = address
)

user_data = {
    "id":1,
    "name":"Divyanshu",
    "address":{
        "street":"321 something",
        "city":"Jaipur",
        "postal_code":"200002"
    }
}
users = User(**user_data)
print(users)
