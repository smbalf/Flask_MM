import os
from dotenv import load_dotenv

import pymongo
from bson import ObjectId

from item_dict import item_dict


load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_HOST"))
db = client.itemData
collection = db.items


filter = {"_id": ObjectId('63c83050832ecf1db41a49c0')}
new_values = { "$set": item_dict}

collection.update_one(filter, new_values)

client.close()
