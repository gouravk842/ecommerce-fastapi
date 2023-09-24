from uuid import UUID

import fastapi
from fastapi import Depends
from pymongo.database import Database
from starlette.requests import Request

from src.common_utility.response_structure import send_response
from src.ecommerce.model.product import Product
from src.ecommerce.service.product import get_product_list_service, add_product_service, get_product_service

product_router = fastapi.APIRouter()


def get_database(request: Request):
    return request.app.db


@product_router.get('/products', response_model=list[Product])
async def get_product_list(db: Database = Depends(get_database)):
    products = get_product_list_service(db)
    return products


@product_router.post("/products", response_model=Product)
def create_product(product: Product, db: Database = Depends(get_database)):
    add_product_service(db, product.dict())
    return send_response(data={"message": "success"})


@product_router.get("/product/{product_id}", response_model=Product)
def get_product(product_id: str, db: Database = Depends(get_database)):
    product = get_product_service(db, UUID(product_id))

    if not product:
        return send_response(status_code=404, error="Product not found")
    return product
