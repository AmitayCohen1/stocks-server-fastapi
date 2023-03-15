from pydantic import BaseSettings
import motor.motor_asyncio
from models import Stock


client = motor.motor_asyncio.AsyncIOMotorClient(
    "", )
database = client.BANK_APP_DB
collection = database.stocks

async def get_stocks():
    stocks = []
    cursor = collection.find({})
    async for stock in cursor:
        stocks.append(Stock(**stock))
    return stocks



async def get_stock(stock_mame):
    response = await collection.find_one({"title": stock_mame})
    return  response

async def post_stock(stock_object):
    response = await collection.insert_one(stock_object)
    return response