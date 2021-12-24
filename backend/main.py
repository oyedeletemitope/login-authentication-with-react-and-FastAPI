
from fastapi import FastAPI
from pydantic import BaseModel
import jwt
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware


SECERT_KEY = "my_secret_key"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 800

test_user = {
   "username": "temitope",
    "password": "temipassword",
     
}

app = FastAPI()

origins = {
    "http://localhost",
    "http://localhost:3000",
}

app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

class LoginItem(BaseModel):
    username: str
    password: str
    
    @app.get("/")
    def read_root():
     return {"Hello": "World"}

@app.post("/login")
async def user_login(loginitem:LoginItem):
    
    
    data = jsonable_encoder(loginitem)
    
    if data['username']== test_user['username'] and data['password']== test_user['password']:
        
        encoded_jwt = jwt.encode(data, SECERT_KEY, algorithm=ALGORITHM)
        return {'token': encoded_jwt}        
    else:
        return {'message':'login failed'}
            
    