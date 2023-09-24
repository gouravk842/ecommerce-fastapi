from datetime import datetime

from pymongo.database import Database

from src.ecommerce.constant import ORDER_COLLECTION
from src.ecommerce.service.product import validate_products_exist, validate_product_quantity, reduce_product_quantity
from src.user.service import validate_user_exists


# Add an order to the database, by validating the user and products
def add_order_service(db: Database, order_data):
    if not validate_user_exists(db, order_data.get("user_id")):
        return 400, "User does not exist"

    product_details = order_data.get("products")
    product_ids = [pd["product_id"] for pd in product_details]
    if not validate_products_exist(db, product_ids):
        return 400, "One or more products do not exist"

    if not validate_product_quantity(db, order_data.get("products")):
        return 400, "One or more products have insufficient quantity"

    saved_instance = db[ORDER_COLLECTION].insert_one(order_data)

    reduce_product_quantity(db, order_data.get("products"))
    message = {
        "status": "success",
        "message": "Order created successfully",
        "order_id": str(saved_instance.inserted_id)
    }

    return 200, message


# Get the order details from the database
def get_order_service(db: Database, order_id):
    try:
        order = db[ORDER_COLLECTION].find_one({"id": order_id})
    except Exception as e:
        order = None
    return order


# Get the list of orders from the database
def get_order_list_service(db: Database, page_number: int, page_size: int):
    start_index = (page_number - 1) * page_size
    orders = list(db[ORDER_COLLECTION].find().skip(start_index).limit(page_size))
    return orders


# Update the quantity of products in a placed order
def update_ordered_product_quantity_service(db: Database, order, updated_products):
    if not validate_products_exist(db, [updated_products["product_id"]]):
        return 400, "One or more products do not exist"

    if not validate_product_quantity(db, [updated_products]):
        return 400, "One or more products have insufficient quantity"

        # Find the product in the products list by product_id
    for product in order["products"]:
        if str(product["product_id"]) == updated_products["product_id"]:
            older_quantity = product["quantity"]
            product["quantity"] = updated_products["quantity"]
            updated_products["quantity"] = older_quantity - updated_products["quantity"]
            break
    order.modified_date = datetime.utcnow()
    db[ORDER_COLLECTION].update_one({"id": order.id}, {"$set": order})

    reduce_product_quantity(db, [updated_products])
    return 200, {"message": "Product quantity updated successfully"}
