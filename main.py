import asyncio
from fastapi import FastAPI
from api.stocks_api import stocks_router
from api.ibkr import IBapi

app = FastAPI()
ib_app = IBapi()

async def ibkr_task():
    await ib_app.connect("127.0.0.1", 7496, 1)
    ib_app.run()

@app.get('/')
def first_test():
    return {"hey" : "you"}

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(ibkr_task())

app.include_router(stocks_router, prefix='/stocks')
