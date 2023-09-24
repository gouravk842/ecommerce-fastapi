from uuid import UUID

import fastapi
from fastapi import Depends, Query
from pymongo.database import Database
from starlette.requests import Request

from src.common_utility.response_structure import send_response
from src.ecommerce.model.order import Order, ProductDetails
from src.ecommerce.service.order import add_order_service, get_order_service, get_order_list_service, \
    update_ordered_product_quantity_service

order_router = fastapi.APIRouter()


def get_database(request: Request):
    return request.app.db


@order_router.post("/order", response_model=Order)
def create_order(order: Order, db: Database = Depends(get_database)):
    status_code, message = add_order_service(db, order.dict())

    if status_code == 400:
        return send_response(status_code=status_code, error=message)

    return send_response(data=message)


@order_router.get("/order/{order_id}", response_model=Order)
def get_order(order_id: str, db: Database = Depends(get_database)):
    order = get_order_service(db, order_id)
    if not order:
        return send_response(status_code=404, error="Order not found")
    return order


@order_router.get("/orders", response_model=list[Order])
def get_order_list(db: Database = Depends(get_database),
                   page: int = Query(1, description="Page number, starting from 1", ge=1),
                   per_page: int = Query(10, description="Items per page", le=100),
                   ):
    order_list = get_order_list_service(db, page, per_page)
    return order_list


@order_router.put("/orders/{order_id}", response_model=Order,
                  description="Update the quantity of products in an order")
async def update_order_products(order_id: UUID, updated_products: ProductDetails,
                                db: Database = Depends(get_database)):
    existing_order = get_order_service(db, order_id)
    if existing_order is None:
        return send_response(status_code=404, error="Order not found")

    status_code, message = update_ordered_product_quantity_service(db, order_id, updated_products)

    if status_code == 400:
        return send_response(status_code=status_code, error=message)
    return send_response(data=message)
