from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(nullable=False)
    price: float = Field(nullable=False)
    available_quantity: int = Field(nullable=False)
    created_date: datetime = Field(default_factory=datetime.utcnow)
    modified_date: datetime = Field(default_factory=datetime.utcnow)






