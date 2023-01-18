import os
from dotenv import load_dotenv

import pymongo
from bson import ObjectId

from building_dict import building_dict


load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_HOST"))
db = client.buildingData
collection = db.buildings


filter = {"_id": ObjectId('63c85e2cb520018002abd631')}
new_values = { "$set": building_dict}

collection.update_one(filter, new_values)

client.close()
