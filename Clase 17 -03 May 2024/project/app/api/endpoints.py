from fastapi import APIRouter,HTTPException
from pydantic import BaseModel  # 
from typing import Dict

router = APIRouter()

# Sample data (in-memory database)
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

inventory = {
    "item1": Item(name="Item 1", description="Description for Item 1", price=9.99, tax=0.18),
    "item2": Item(name="Item 2", description="Description for Item 2", price=14.99, tax=0.18),
}

# Get all items
@router.get("/items/")
async def read_items():
    return inventory

# Get one
@router.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[item_id]

# Crear new item
@router.post("/items/")
async def create_item(item: Item):
    inventory[item.name.lower()] = item
    return {"message": "Item created successfully"}

# Update un item que existe
@router.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    inventory[item_id] = item
    return {"message": "Item updated successfully"}

# Borrar un item
@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    del inventory[item_id]
    return {"message": "Item deleted successfully"}
# En project: uvicorn main:app --reload