from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


def int_to_roman(num: int):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += symb[i]
            num -= val[i]
        i += 1
    return roman_num


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("converter.html", {"request": request})


@app.post("/convert", response_class=HTMLResponse)
async def convert(request: Request):
    form = await request.form()
    arabic_number = form.get("arabic_number")
    roman_number = int_to_roman(int(arabic_number))
    return templates.TemplateResponse(
        "converter.html",
        {"request": request, "arabic_number": arabic_number, "roman_number": roman_number}
    )
