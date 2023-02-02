from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from src.api.services.product import GetAllProducts
from src.api.schemas.product import GetAllProductsRequest, GetAllProductsResponse

views = APIRouter()

templates = Jinja2Templates(directory="src/templates")


@views.get("/", response_class=HTMLResponse)
async def get_all_products_page(
    request: Request, service: GetAllProducts = Depends(GetAllProducts)
):
    result = await service.process(GetAllProductsRequest())
    return templates.TemplateResponse(
        "products.html", {**result.dict(), "request": request}
    )
