from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from os import path

from soup import soupSolver

app = FastAPI()

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
TEMPLATES_DIR = path.join(BASE_DIR, "frontend", "templates")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Model for alphabet soup
class Soup(BaseModel):
    soup: str
    words: str
    size: Optional[int] = 14

# Shows Main Page
@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    # return {"Hello": "World"}
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/solver")
def solver(soup: Soup):

    wordsFound = soupSolver(soup.soup, soup.words, soup.size)

    return wordsFound