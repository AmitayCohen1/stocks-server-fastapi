from typing import List
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., description="User's name")
    email: str = Field(..., description="User's email address")
    phone: str = Field(..., description="User's phone number")

class Stock(BaseModel):
    stock: str = Field(..., description="Stock name")
    current_price: int = Field(..., description="Current price") ##might not needed. when you fetch the data you can compare the highest price, but I dont think we need it. 
    highest_price: int = Field(..., description="Highest price")
    percent_drop_15: List[User] = Field(..., description="Subscribers for 15% drop")
    percent_drop_10: List[User] = Field(..., description="Subscribers for 10% drop")
    percent_drop_5: List[User] = Field(..., description="Subscribers for 5% drop")


class Todo(BaseModel):
    title: str
    description: str