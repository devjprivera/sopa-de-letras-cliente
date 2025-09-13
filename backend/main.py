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

# Shows Main Page
@app.get("/", response_class=HTMLResponse)
def main(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def solver(request: Request, words: str = Form(...), soup: str = Form(...)):

    soup = soup.replace("\r\n", " ")
    wordsFound = soupSolver(soup, words)

    return templates.TemplateResponse("index.html", {"request": request, "wordsFound": wordsFound})