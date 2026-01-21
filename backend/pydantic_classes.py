from datetime import datetime, date, time
from typing import List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

############################################
# Classes are defined here
############################################
class AuthorCreate(BaseModel):
    name: str
    books: List[int]  # N:M Relationship

class LibraryCreate(BaseModel):
    name: str
    books: List[int]  # N:M Relationship

class BookCreate(BaseModel):
    stock: int
    release: date
    time: time
    pages: int
    title: str
    price: float
    authors: List[int]  # N:M Relationship
    library: List[int]  # N:M Relationship

    @field_validator('pages')
    @classmethod
    def validate_pages_1(cls, v):
        """OCL Constraint: constraint_Book_0_1"""
        if not (v > 10):
            raise ValueError('pages must be > 10')
        return v
