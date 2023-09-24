from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from src.user.model import Address


class ProductDetails(BaseModel):
    product_id: UUID
    quantity: int


class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID = Field(nullable=False)
    products: list[ProductDetails] = Field(nullable=False)
    total_price: float
    address: Address = Field(nullable=False)
    created_date: datetime = Field(default_factory=datetime.utcnow)
    modified_date: datetime = Field(default_factory=datetime.utcnow)
