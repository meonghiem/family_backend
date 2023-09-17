from typing import Union
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.configs.auth_config import Settings
from src.controllers.auth.auth_controller import router as user_router
from src.controllers.products.product_controller import router as product_router
from src.controllers.invoices.invoice_controller import router as invoice_router
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from src.utils.utils import CustomORJSONResponse
#create table into db
# BaseModel.metadata.create_all(bind=engine)

app = FastAPI(default_response_class=CustomORJSONResponse)
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()

# exception handler for authjwt
# in production, you can tweak performance using orjson response
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )



app.include_router(user_router, prefix="/api", tags=['User'])
app.include_router(product_router, prefix="/api", tags=['Product'])
app.include_router(invoice_router, prefix="/api", tags=['Invoice'])

@app.get("/")
async def hello_world():
    return "hello_world"

if __name__ == '__main__':
    uvicorn.run("main:app", port =8000, host="localhost")

