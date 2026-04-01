# app/models/product.py
from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):  # This is an Entity
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock = Column(Integer)

    def reduce_stock(self, quantity: int):  # Business rule inside Entity
        if self.stock < quantity:
            raise ValueError("Insufficient stock")
        self.stock -= quantity