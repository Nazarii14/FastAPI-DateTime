from fastapi import FastAPI
import uvicorn
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
