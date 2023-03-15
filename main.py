from typing import Union
from fastapi import FastAPI
from api.stocks_api import stocks_router
from api.ibkr import IBapi
from ibapi.contract import Contract
from ibapi.common import BarData


app = FastAPI()

ib_app = IBapi()
ib_app.connect("127.0.0.1", 7496, 1)

ib_app.run()


@app.get('/')
def first_test():
    return {"hey" : "you"}



app.include_router(stocks_router, prefix='/stocks')