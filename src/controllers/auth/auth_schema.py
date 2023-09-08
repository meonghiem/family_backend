from pydantic import BaseModel
class LoginRequest(BaseModel):
    username: str
    password: str

class SignUpRequest(BaseModel):
    username: str
    password: str
    email: str
    phone: str
    address: str