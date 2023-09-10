from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from src.controllers.auth.auth_schema import LoginRequest, SignUpRequest
from src.controllers.auth import user_service
from src.utils.constants import ROLE
from src.utils.exceptions import PermissionDenied
router = APIRouter()

@router.post("/login")
async def login(
    data: LoginRequest,
    db: AsyncSession= Depends(get_session),
    auth: AuthJWT = Depends()
):
    username = data.username
    password = data.password
    account = await user_service.check_account(db, username, password)
    if not account:
        raise HTTPException(detail ='Account is not exist', status_code=404)
    id= account.id
    obj = {
        "id": account.id,
        "username": account.username,
    }
    shop = await user_service.check_shop(db, id)
    if not shop:
        obj["role_id"] = ROLE.USER
    else:
        obj["role_id"] =ROLE.SHOP
    token = await user_service.create_token(auth, obj)
    return token
    
    
@router.post("/signup")
async def create(
    data: SignUpRequest,
    db: AsyncSession= Depends(get_session),
    auth: AuthJWT = Depends() 
):
    id = await user_service.create_customer(db, data)
    customer = await user_service.get_customer(db, id)
    # obj = {
    #     "id":  customer.id,
    #     "username": customer.username,
    #     "role_id": ROLE.USER,
    # }
    # token = await user_service.create_token(auth, obj)
    return {"message": "success"}

@router.get('/refresh_token')
async def refresh_token(auth: AuthJWT = Depends()):
    auth.jwt_refresh_token_required()
    current_user = auth.get_jwt_subject()
    new_access_token = auth.create_access_token(subject=current_user)
    return {"access_token": new_access_token}

    