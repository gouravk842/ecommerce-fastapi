# FastAPI E-commerce Backend

## Overview

This project serves as the backend implementation for an e-commerce website, utilizing the FastAPI framework and MongoDB database. The project follows mvc architecture and is organized into modules for products, orders, and users. The project also includes unit tests for each module.

## Project Directory Structure

```plaintext
fastApiProject
├───src
│   ├───common_utility
│   ├───ecommerce
│   │   ├─controller
│   │   ├─model
│   │   └─service
│   ├───user
│   │   ├─controller
│   │   ├─model
│   │   └─service
│   └───app_config.py
│   └───database.py
│   └───main.py
├───test
├───README.md
├───requirements.txt
```

# Project Modules
The project is organized into two primary modules:

### Ecommerce
The ecommerce module focuses on product-related operations, facilitating efficient handling of product data.

### User
The user module is dedicated to user-related operations, including tasks like user registration and authentication.

### Database Integration
MongoDB is the chosen database solution for this project. The connection to the MongoDB database is established within the database.py file. This connection is subsequently utilized in the service layer of each module, enabling seamless data interactions.

# API Endpoints

Here are the endpoints and operations supported by this API:

## Products

### Get Product List
- **Summary**: Retrieve a list of products.
- **HTTP Method**: GET
- **Endpoint**: `/products`
- **Response**: 200 OK
  - Content: JSON array of products (See [Product-Output](#product-output) schema)

### Create Product
- **Summary**: Create a new product.
- **HTTP Method**: POST
- **Endpoint**: `/products`
- **Request Body**: JSON data (See [Product-Input](#product-input) schema)
- **Response**: 
  - 200 OK
    - Content: JSON representation of the created product (See [Product-Output](#product-output) schema)
  - 422 Unprocessable Entity
    - Content: Validation error details (See [HTTPValidationError](#httpvalidationerror) schema)

### Get Product
- **Summary**: Retrieve a specific product.
- **HTTP Method**: GET
- **Endpoint**: `/product/{product_id}`
- **Path Parameter**: `product_id` (string)
- **Response**: 
  - 200 OK
    - Content: JSON representation of the product (See [Product-Output](#product-output) schema)
  - 422 Unprocessable Entity
    - Content: Validation error details (See [HTTPValidationError](#httpvalidationerror) schema)

## Orders

### Create Order
- **Summary**: Create a new order.
- **HTTP Method**: POST
- **Endpoint**: `/order`
- **Request Body**: JSON data (See [Order-Input](#order-input) schema)
- **Response**: 
  - 200 OK
    - Content: JSON representation of the created order (See [Order-Output](#order-output) schema)
  - 422 Unprocessable Entity
    - Content: Validation error details (See [HTTPValidationError](#httpvalidationerror) schema)

### Get Order
- **Summary**: Retrieve a specific order.
- **HTTP Method**: GET
- **Endpoint**: `/order/{order_id}`
- **Path Parameter**: `order_id` (string)
- **Response**: 
  - 200 OK
    - Content: JSON representation of the order (See [Order-Output](#order-output) schema)
  - 422 Unprocessable Entity
    - Content: Validation error details (See [HTTPValidationError](#httpvalidationerror) schema)

### Get Order List
- **Summary**: Retrieve a list of orders.
- **HTTP Method**: GET
- **Endpoint**: `/orders`
- **Query Parameters**:
  - `page` (integer) [optional] - Page number (starting from 1)
  - `per_page` (integer) [optional] - Items per page (maximum 100)
- **Response**: 
  - 200 OK
    - Content: JSON array of orders (See [Order-Output](#order-output) schema)
  - 422 Unprocessable Entity
    - Content: Validation error details (See [HTTPValidationError](#httpvalidationerror) schema)

### Update Order Products
- **Summary**: Update the quantity of products in an order.
- **Description**: This operation allows you to modify product quantities in an existing order.
- **HTTP Method**: PUT
- **Endpoint**: `/orders/{order_id}`
- **Path Parameter**: `order_id` (string, format: uuid)
- **Request Body**: JSON data (See [ProductDetails](#productdetails) schema)
- **Response**: 
  - 200 OK
    - Content: JSON representation of the updated order (See [Order-Output](#order-output) schema)
  - 422 Unprocessable Entity
    - Content: Validation error details (See [HTTPValidationError](#httpvalidationerror) schema)

## User

### Create User
- **Summary**: Create a new user.
- **HTTP Method**: POST
- **Endpoint**: `/user`
- **Request Body**: JSON data (See [User-Input](#user-input) schema)
- **Response**: 
  - 200 OK
    - Content: JSON representation of the created user (See [User-Output](#user-output) schema)
  - 422 Unprocessable Entity
    - Content: Validation error details (See [HTTPValidationError](#httpvalidationerror) schema)

