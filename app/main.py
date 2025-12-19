from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.services import analyze_sentiment
from app.stats import update_stats, get_stats

app = FastAPI(title="Sentiment Panda 🐼")

# static ve templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None, "text": ""}
    )


@app.post("/analyze_ui", response_class=HTMLResponse)
async def analyze_ui(request: Request, text: str = Form(...)):
    sentiment, score = analyze_sentiment(text)
    update_stats(sentiment)
    result = {"sentiment": sentiment, "score": score}

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result, "text": text}
    )


@app.get("/stats")
def stats():
    return get_stats()
