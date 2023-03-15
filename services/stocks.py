from pydantic import BaseSettings
import motor.motor_asyncio
from models import Stock


class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017/"
    database_name: str = "stocks_db"


settings = Settings()

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
database = client[settings.database_name]
collection = database.stocks


async def get_stocks():
    stocks = []
    cursor = collection.find({})
    async for stock in cursor:
        stocks.append(Stock(**stock))
    return stocks


async def get_stock(stock_name):
    response = await collection.find_one({"name": stock_name})
    if response:
        return Stock(**response)


async def create_stock(stock: Stock):
    response = await collection.insert_one(stock.dict())
    return response


async def update_stock(stock: Stock):
    response = await collection.replace_one({"name": stock.name}, stock.dict())
    return response


async def delete_stock(stock_name: str):
    response = await collection.delete_one({"name": stock_name})
    return response
