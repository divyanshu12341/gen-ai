from pydantic import BaseModel 
from typing import Optional,List

class Company(BaseModel):
    name:str
    address:Optional[Address] = None

class Employee(BaseModel):
    name:str
    company:Optional[Company] = None

class TextContent(BaseModel):
    type:str = "text"
    content:str 

class ImageContent(BaseModel):
    type:str = "Image"
    url:str
    alt_text:str 

class Article(BaseModel):
    title:str 
    sections: List[Union[TextContent,ImageContent]]

class Country(BaseModel): 
    name:str 
    code:str 

class State(BaseModel):
    name:str 
    country:Country 

class City(BaseModel):
    name:str 
    state:State 

class Address(BaseModel):
    street:str
    city: City
    postal_code:str 

class Organization(BaseModel):
    name:str 
    head_quarter:Address
    branches:List[Address] = []


#Best practices 
# Model organization 
# 1)Define leaf models first --> models with no dependencies 
# 2) Build upward --> Gradually compose more complex models 
# 3) Use clear naming --> Make relationships obvious 
# 4) Group related models --> 

# Performance considerations 
# 1) Deep nesting impacts performance --> keep reasonable depth 
# 2) Large list of nested models --> consider paginations 
# 3) Circular references --> Use carefully can cause memory issues 
# 4) Lazy loading --> consider for expensive nested computations 

# Data modelling tips: 
# 1) Model real world relationships --> Mirror your domain structure 
# 2) Use optional appropriately --> not all relationships are required 
# 3) Consider union types --> for polymorphic relationships 
# 4) Validate business rules --> use model validators for cross model logic

