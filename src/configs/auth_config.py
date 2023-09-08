from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


# in production you can use Settings management
# from pydantic to get secret key from .env
class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
