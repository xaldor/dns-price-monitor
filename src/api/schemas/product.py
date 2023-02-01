from pydantic import BaseModel
from pydantic import AnyHttpUrl

from src.schemas import Product, ProductId


class AddProductRequest(BaseModel):
    url: AnyHttpUrl


class AddProductResponse(BaseModel):
    product: Product


class RemoveProductRequest(BaseModel):
    id: ProductId


class RemoveProductResponse(BaseModel):
    pass
