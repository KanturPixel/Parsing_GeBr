from pymongo import MongoClient
from itemadapter import ItemAdapter

class BookparserPipeline:
    def __init__(self):
        self.client = MongoClient("localhost:27017")
        self.db = self.client["books"]

    def process_item(self,item, spider):
        id = item.get('url')
        item['_id'] = id.split('-')[-1].replace('/', '')
        self.db[spider.name].update_one({'_id': {"$eq": item['_id']}}, {'$set': item}, upsert=True)
        print()
        return item