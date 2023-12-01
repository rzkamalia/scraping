# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# note: 
# variable ITEM_PIPELINES in setting.py by default will looks like bellow
# ITEM_PIPELINES = {
#    "scrapy_project.pipelines.ScrapyProjectPipeline": 300,
# }
# if we add  > "scrapy_project.pipelines.NewAction": 200, < 
# that means NewAction will be executed first then ScrapyProjectPipeline.
# this because lower number is high priority

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class MongodbPipeline:
    def __init__(self):
        self.mongo_url = "mongodb+srv://daesungjinwoo:AMELpalelo8@cluster-one.2sbakwz.mongodb.net/?retryWrites=true&w=majority"
        self.mongo_db = "first_database"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
        
    def process_item(self, item, spider):
        country = item["country"]
        collection_name = f"collection_{country}"

        collection = self.db[collection_name]
        collection.insert_one(dict(item))
        return item
