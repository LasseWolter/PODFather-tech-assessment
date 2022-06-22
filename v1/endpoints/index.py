from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime

# from sqlalchemy.orm import Session

from app.core import schemas

router = APIRouter()


@router.get("/")
def read_items() -> Any:
    """
    Show welcome message
    """
    return "Welcome to this PODFather Assessment API"
