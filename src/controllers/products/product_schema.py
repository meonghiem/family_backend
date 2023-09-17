from pydantic import BaseModel

class ProductCreate(BaseModel):
    shop_id: int
    img_url: str | None
    price: float
    name: str
    description: str | None
    