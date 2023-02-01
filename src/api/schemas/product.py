from pydantic import BaseModel
from pydantic import AnyHttpUrl

from src.schemas import Product


class AddProductRequest(BaseModel):
    url: AnyHttpUrl


class AddProductResponse(BaseModel):
    product: Product
