from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Root endpoint
@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the FastAPI application!"}

#Example GET API with a parameter
@app.get("/user")
def user_profile():
    return {"username": "Nithya", 
            "age": 30, 
            "email": "nithyashenbagaraj07@gmail.com"
            }

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if(user_id==1):
        return { "username": "Nithya",
                "age": 27, 
                "email": "nithyashenbagaraj07@gmail.com"
                }
    else:
        return {"name": "Nty"+str(user_id),
                "age": 27, 
                "email": "nithyashenbagaraj07@gmail.com"
                }


#post API to create a new user

class User(BaseModel):
    username: str
    age: int
    email: str

users = []

@app.post("/user")
def create_user(user: User):
    users.append(user.dict())
    return {"message": "User created successfully","total_users": len(users), "user": user}
#download postman from browser and test the API using postman. 
# You can also use curl command to test the API.
#https://youtu.be/Z8zEtb7hHAY?si=oMXCFw600sjV63us