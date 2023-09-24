from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, EmailStr, validator
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Address(BaseModel):
    pincode: str = Field(nullable=False)
    city: str = Field(nullable=False)
    country: str = Field(nullable=False)


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(nullable=False)
    email: EmailStr = Field(unique=True, nullable=False)
    password: str = Field(nullable=False)
    address: Address = Field(nullable=False)
    created_date: datetime = Field(default_factory=datetime.utcnow)
    modified_date: datetime = Field(default_factory=datetime.utcnow)

    @validator("password")
    def hash_password(cls, v):
        return pwd_context.hash(v)
