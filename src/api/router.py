from fastapi import APIRouter
from fastapi import Depends

from .schemas.product import (
    AddProductRequest,
    AddProductResponse,
    RemoveProductRequest,
    RemoveProductResponse,
    GetAllProductsRequest,
    GetAllProductsResponse,
)

from .services.product import AddProduct, RemoveProduct, GetAllProducts

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


@router.get("/products")
async def get_all_products_in_monitor_list(
    service: GetAllProducts = Depends(GetAllProducts),
) -> GetAllProductsResponse:
    return await service.process(GetAllProductsRequest())
