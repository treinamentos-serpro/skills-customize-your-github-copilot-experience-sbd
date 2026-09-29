from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(gt=0)


books = [
    Book(id=1, title="Kindred", author="Octavia E. Butler", year=1979),
    Book(id=2, title="The Left Hand of Darkness", author="Ursula K. Le Guin", year=1969),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}