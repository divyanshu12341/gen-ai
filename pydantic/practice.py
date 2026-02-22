# from pydantic import BaseModel


# class User(BaseModel):
#     id:int
#     name:str
#     is_active:bool

# user1 = User(id = 1,name = "Divyanshu",is_active = True)
# print(user1)
# #auto-coercion
# user2 = User(id='2',name = 'Devesh', is_active = False)
# print(user2)
# -------------------------------------------------------------------------------------------
# from pydantic import BaseModel, ValidationError


# class Product(BaseModel):
#     id:int
#     name:str
#     price:float

# try:
#     p = Product(
#         id = 'nan',
#         name = None,
#         price = 5.0)
# except ValidationError as e:
#     print(e.error_count())
#     for err in e.errors():
#         print("Msg is ",err['msg'])
#         print("Path is ",err['loc'])

# -------------------------------------------------------------------------------------------
from typing import Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    name:str = Field(
        ...,
        min_length = 3,
        max_length = 50,
        description = "Full Name",
        examples = ['Divyanshu Jain'])
    salary:float = Field(
        ...,
        ge=10000,
        le=100000,
        description = "This is salary of an employee"
    )
    department:Optional[str] = Field(
        default = "General"
    )
    user_id:int = Field(...,alias = "userId")

emp1 = Employee(name = "Divyanshu",salary = 10001,department = "HR",userId=100)
print(emp1)
