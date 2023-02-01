from fastapi import APIRouter
from fastapi import Depends

from .schemas.product import AddProductRequest, AddProductResponse
from .services.product import AddProduct

router = APIRouter()


@router.post("/products")
async def add_product_to_monitor_list(
    data: AddProductRequest, service: AddProduct = Depends(AddProduct)
) -> AddProductResponse:
    return await service.process(data)
