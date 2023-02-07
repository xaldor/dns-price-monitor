from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form

from src.api.services.product import GetAllProducts, AddProduct
from src.api.schemas.product import GetAllProductsRequest, AddProductRequest

from src.dns.exceptions import InvalidUrl

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


@views.post("/products", response_class=HTMLResponse)
async def post_new_product(
    request: Request, service: AddProduct = Depends(AddProduct), product_url=Form()
):
    try:
        result = await service.process(AddProductRequest(url=product_url))
    except InvalidUrl:
        return templates.TemplateResponse("fail.html", {"request": request})
    else:
        return templates.TemplateResponse(
            "success.html", {**result.dict(), "request": request}
        )


@views.get("/add_product", response_class=HTMLResponse)
async def add_product(request: Request):
    return templates.TemplateResponse("add_product.html", {"request": request})
