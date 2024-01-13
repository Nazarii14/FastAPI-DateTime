from fastapi import FastAPI

from calculations import *

app = FastAPI()


@app.get("/info")
async def info():
    print(get_all_info())
    return get_all_info()


@app.get("/month")
async def month():
    return get_month_info()


@app.get("/year")
async def year():
    return get_year_info()
