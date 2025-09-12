from fastapi import FastAPI
from soup import soupSolver
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model for alphabet soup
class Soup(BaseModel):
    soup: str
    words: str
    size: Optional[int] = 14

# Shows Main Page
@app.get("/")
def main():
    return {"Hello": "World"}

@app.post("/solver")
def solver(soup: Soup):

    wordsFound = soupSolver(soup.soup, soup.words, soup.size)

    return wordsFound