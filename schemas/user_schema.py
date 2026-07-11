from pydantic import BaseModel, EmailStr

class UserRegisterSchema(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    age: int
    img_url: str

class UserLoginSchema(BaseModel):
    username: str
    password: str