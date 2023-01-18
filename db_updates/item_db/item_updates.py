import pymongo
from bson import ObjectId
from item_dict import item_dict

item_db = client.itemData
item_collection = item_db.items


filter = {"_id": ObjectId('63c83050832ecf1db41a49c0')}
new_values = { "$set": item_dict}

item_collection.update_one(filter, new_values)

client.close()
