from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Your dictionary
items = {
    "gps1": "Bob",
    "gps2": "Sam",
    "gps3": "Mia",
}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to the test dashboard"})

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.post("/gear/{id}", response_class=HTMLResponse)
async def add_item(request: Request, id: str):
    items[id] = id

@app.get("/gear", response_class=HTMLResponse)
async def list_items(request: Request):
    return templates.TemplateResponse("gear.html", {
        "request": request,
        "items": items
    })
