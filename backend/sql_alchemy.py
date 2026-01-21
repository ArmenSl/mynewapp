import enum
from typing import List, Optional
from sqlalchemy import (
    create_engine, Column, ForeignKey, Table, Text, Boolean, String, Date, 
    Time, DateTime, Float, Integer, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped, mapped_column, relationship
)
from datetime import datetime as dt_datetime, time as dt_time, date as dt_date

class Base(DeclarativeBase):
    pass



# Tables definition for many-to-many relationships
books_1 = Table(
    "books_1",
    Base.metadata,
    Column("authors", ForeignKey("author.id"), primary_key=True),
    Column("books", ForeignKey("book.id"), primary_key=True),
)
books = Table(
    "books",
    Base.metadata,
    Column("library", ForeignKey("library.id"), primary_key=True),
    Column("books", ForeignKey("book.id"), primary_key=True),
)

# Tables definition
class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Library(Base):
    __tablename__ = "library"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    pages: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    release: Mapped[dt_date] = mapped_column(Date)
    time: Mapped[dt_time] = mapped_column(Time)


#--- Relationships of the author table
Author.books: Mapped[List["Book"]] = relationship("Book", secondary=books_1, back_populates="authors")

#--- Relationships of the library table
Library.books: Mapped[List["Book"]] = relationship("Book", secondary=books, back_populates="library")

#--- Relationships of the book table
Book.authors: Mapped[List["Author"]] = relationship("Author", secondary=books_1, back_populates="books")
Book.library: Mapped[List["Library"]] = relationship("Library", secondary=books, back_populates="books")

# Database connection
DATABASE_URL = "sqlite:///Class_Diagram.db"  # SQLite connection
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
Base.metadata.create_all(engine, checkfirst=True)