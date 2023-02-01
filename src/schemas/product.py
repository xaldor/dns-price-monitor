from pydantic import BaseModel, AnyHttpUrl, confloat
from typing import TypeAlias, Optional


ProductId: TypeAlias = int
ProductTitle: TypeAlias = str
ProductUrl: TypeAlias = AnyHttpUrl
ProductDescription: TypeAlias = Optional[str]
ProductRating: TypeAlias = Optional[confloat(ge=0.0, le=1.0)]


class ProductInfo(BaseModel):
    title: ProductTitle
    url: ProductUrl
    description: ProductDescription
    rating: ProductRating


class Product(ProductInfo):
    id: ProductId

    class Config:
        orm_mode = True
