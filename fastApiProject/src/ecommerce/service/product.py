from pymongo.database import Database
from src.ecommerce.constant import PRODUCT_COLLECTION


# Get the list of products from the database
def get_product_list_service(db: Database):
    products = list(db[PRODUCT_COLLECTION].find())
    return products


# Add a product to the database
def add_product_service(db: Database, product_data):
    db[PRODUCT_COLLECTION].insert_one(product_data)
    return product_data


# Get the product details from the database
def get_product_service(db: Database, product_id):
    try:
        product = db[PRODUCT_COLLECTION].find_one({"id": product_id})
    except Exception as e:
        product = None
    return product


# Check if the products in the order exist in the database
def validate_products_exist(db: Database, product_ids):
    products = db[PRODUCT_COLLECTION].find({"id": {"$in": product_ids}})
    return len(list(products)) == len(product_ids)


# Check if the quantity of products in the database is sufficient for an order
def validate_product_quantity(db: Database, product_details):
    for pd in product_details:
        product = db[PRODUCT_COLLECTION].find_one({"id": pd["product_id"]})
        if product is None or pd["quantity"] > product["available_quantity"]:
            return False
    return True


# Reduce the quantity of products in the database after an order is placed successfully
def reduce_product_quantity(db: Database, product_details):
    for pd in product_details:
        db[PRODUCT_COLLECTION].update_one(
            {"id": pd["product_id"]},
            {"$inc": {"available_quantity": -pd["quantity"]}}
        )
