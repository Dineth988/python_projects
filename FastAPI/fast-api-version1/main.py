from fastapi import FastAPI, Query, HTTPException
from enum import Enum, StrEnum
from typing import Annotated


app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "hello world from fastapi"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return item_id


# class Modelname(StrEnum):
#     alexnet: str = "Alexnet"
#     kiwi: str = "kiwinet"

# QType = Annotated[str | None, Query(max_length=10)]

# @app.get("/models/{modelname}")
# async def print_model(modelname: QType = None):
#     if modelname == Modelname.alexnet.value:
#         return modelname

# from fastapi import FastAPI
from pydantic import BaseModel

# class VerifyModel(BaseModel):
#     name: str
#     age: int

# app = FastAPI()

# @app.post("/items")
# async def get_items(item: VerifyModel):
#     if item.name is not "dineth":
#         item.name = "dilmin"
#     return item

@app.get("/")
async def root():
    return "Welcome"

class Book(BaseModel):
    title: str
    author: str
    price: float
    in_stock: bool = True

books_db = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 12.99, "in_stock": True},
    {"id": 2, "title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": False},
]

@app.get("/books")
async def get_books():
    return books_db

@app.get("/books/search")
async def get_books(author: str | None = None, max_price: float | None = None):
    if author is not None:
        results = [book for book in books_db if author.lower() in book["author"].lower()]
    if max_price is not None:
        results = [b for b in results if b["price"] <= max_price]
    return results

@app.get("/books/{book_id}")
async def get_books(book_id: int):
    for book in books_db:
        if book_id == book["id"]:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


