from typing import Optional 
from pydantic import BaseModel,Field 

class Employee(BaseModel):
    id:int
    name:str=Field(
        ...,  #... means required 
        min_length = 3,
        max_length = 50,
        description = "Employee name",
        examples = "Divyanshu Jain"
    )
    department:Optional[str] = "General"
    #ge gt le 
    salary:float = Field(
        ...,
        ge = 10000, #ge means greater than or equal to,
        le = 100000,
        description = "Annual salaries in USD"
        
    )

class User(BaseModel):
    email:str = Field(
        ...,
        regex = r''
    )
    phone:str = Field()
    age:int = Field(
        ...,
        ge = 0,
        le = 150,
        description = "Age in years"
    )
    discount:float = Field(
        ...,
        ge=0,
        le=100,
        description = "Discount percentage"
    )
    
    