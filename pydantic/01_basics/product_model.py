from pydantic import BaseModel


class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True

product_1 = Product(id=1,name = "Laptop",price = 99.99,in_stock = True)
product_2 = Product(id=2,name="Headphones",price = 24.33)
print(product_2)
# Always use type annotations in pydantic 
# Set sensible default as well 
# Automatic conversion by pydantic it tries best 
# "true" --> True 

