from dotenv import dotenv_values
from pymongo import MongoClient

env = dotenv_values(".env")
print(env['HOST'])
HOST = env["HOST"]
client = MongoClient(HOST)
db = client.DunkerDB.dunkers

