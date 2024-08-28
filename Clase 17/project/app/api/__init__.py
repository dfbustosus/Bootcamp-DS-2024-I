from fastapi import APIRouter
from . import endpoints

router = APIRouter()

# Include route definitions from endpoints module
router.include_router(endpoints.router)