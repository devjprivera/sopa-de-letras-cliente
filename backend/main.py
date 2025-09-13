from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
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

    if not words or not soup:
        error = "Llena todos los campos"
        return templates.TemplateResponse("index.html", {"request": request, "error": error, "soup": soup, "words": words})

    soup = soup.replace("\r\n", " ").upper()
    words = words.upper()
    wordsFound = soupSolver(soup, words)

    return templates.TemplateResponse("index.html", {"request": request, "wordsFound": wordsFound})