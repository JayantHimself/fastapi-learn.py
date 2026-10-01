from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI ()

@app.get("/")
def home():
    return {"message":"hello jayy"} 

@app.get("/about")
def about():
    return {
        "this is about page"
    }

@app.get("/users/{user_id}")
def get_users(user_id:int):
    return {
        "user_id":user_id
        }

@app.get("/items")
def get_users(name: str =None ,price: int=0):
    return {
        "name":name,
        "price":price,
    }

class user(BaseModel):
    name:str
    age:int

@app.post("/create_user")
def create_user(user:user):
    return{
        "message":"user created"
        "data".user
    }

class address(BaseModel):
    city:str
    pincode:int


class userrs(BaseModel):
    naam:str
    adddress:address

@app.post("/ussers")
def ussers(ussers:userrs):
    return{
        userrs
    }

