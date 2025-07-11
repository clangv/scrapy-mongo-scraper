# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import hashlib
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter #wraps different data containers to handle them in a uniform manner. The package was installed as a dependency of Scrapy.
from scrapy.exceptions import DropItem
class MongoPipeline:
    COLLECTION_NAME = "books" #specifies the name of the MongoDB collection where you want to store the items. This should match the name of the collection that you set up earlier.

    def __init__(self, mongo_uri, mongo_db): #initializes the pipeline with the MongoDB URI and database name. You can access this information because you’re fetching it from the Crawler using the .from_crawler() class method.
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler): #is a class method that gives you access to all core Scrapy components, such as the settings. In this case, you use it to retrieve the MongoDB settings from settings.py through the Scrapy crawler.
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
        )
    
    def open_spider(self,spider): # opens a connection to MongoDB when the spider starts.
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider): #closes the MongoDB connection when the spider finishes.
        self.client.close()

    def process_item(self, item, spider): #inserts each scraped item into the MongoDB collection. This method usually contains the core functionality of a pipeline.
        item_id =self.compute_item_id(item)
        item_dict = ItemAdapter(item).asdict()

        self.db[self.COLLECTION_NAME].update_one(
            filter={"_id": item_id},
            update={"$set": item_dict},
            upsert=True
        )
        return item
        # if self.db[self.COLLECTION_NAME].find_one({"_id": item_id}):
        #     raise DropItem("Duplicate item found: {item}")
        # else:
        #     item["_id"] = item_id
        #     self.db[self.COLLECTION_NAME].insert_one(ItemAdapter(item).asdict())
        #     return item
            
    def compute_item_id(self, item):
        url = item["url"]
        return hashlib.sha256(url.encode("utf-8")).hexdigest()
# class BooksPipeline:
#     def process_item(self, item, spider):
#         return item
