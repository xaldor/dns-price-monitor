from fastapi import APIRouter
from fastapi import Depends

from .schemas.product import (
    AddProductRequest,
    AddProductResponse,
    RemoveProductRequest,
    RemoveProductResponse,
)

from .services.product import AddProduct, RemoveProduct

router = APIRouter()


@router.post("/products")
async def add_product_to_monitor_list(
    data: AddProductRequest, service: AddProduct = Depends(AddProduct)
) -> AddProductResponse:
    return await service.process(data)


@router.delete("/products/{product_id}")
async def delete_product_from_monitor_list(
    product_id: int, service: RemoveProduct = Depends(RemoveProduct)
) -> RemoveProductResponse:
    return await service.process(RemoveProductRequest(id=product_id))
