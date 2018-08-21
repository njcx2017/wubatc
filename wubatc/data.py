import pymongo
from scrapy.conf import settings


class WubatcPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(settings.get('MONGODB_SERVER'),settings.get('MONGODB_PORT'))
        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]
        
        
	
        
	
    def process_item(self, item, spider):
        self.collection.find()
