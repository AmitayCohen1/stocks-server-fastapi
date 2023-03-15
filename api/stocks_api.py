from fastapi import APIRouter, HTTPException
from services.stocks import (get_stocks, get_stock, post_stock)
from models import Stock

stocks_router = APIRouter()

#Get all stocks
@stocks_router.get('/')
async def get_all_stocks():
    response = await get_stocks()
    return response


#Get Single Stock
@stocks_router.get('/{stock_name}',  response_model=Stock)
async def get_single_stock(stock_name):
    response = await get_stock(stock_name)
    if response:
        return response
    raise HTTPException(404, {'couldnt find that stock!': stock_name},)

    
#Post Single Stock
@stocks_router.post('/{stock_object}', response_model=Stock)
async def post_single_stock(stock_object):
    response = post_stock(stock_object)
    if response: 
        return response
    raise HTTPException(400, "Something went wrong")
