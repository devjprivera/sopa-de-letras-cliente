from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from os import path

from soup import soupSolver

app = FastAPI()

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

TEMPLATES_DIR = path.join(BASE_DIR, "frontend", "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

STATIC_DIR = path.join(BASE_DIR, "frontend", "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Shows Main Page
@app.get("/", response_class=HTMLResponse)
def main(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
def solver(request: Request, words: str = Form(...), soup: str = Form(...)):

    # wordsFound = soupSolver(soup.soup, soup.words, soup.size)
    # wordsFound = {
    #     "words": soup.words,
    #     "soup": soup.soup,
    # }

    return {"words": words, "soup": soup}