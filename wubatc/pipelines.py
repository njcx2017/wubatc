# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#from scrapy.exporters import JsonItemExporter
import pymongo
from scrapy.conf import settings


class WubatcPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(settings.get('MONGODB_SERVER'),settings.get('MONGODB_PORT'))
        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]
        	        
	
    def process_item(self, item, spider):
#        self.collection.insert(dict(item))
#        return item


        firstdata = self.collection.find({},{"link":1,"_id":0}).limit(20)
        linked =item['link']

        
        isrepeat = 0
        for i in firstdata:
            
            if i['link'] == linked:                
                isrepeat = 1
                                      
        if isrepeat == 0:
            self.collection.insert(dict(item))
            return item
            
        else:
            print('chongfu')
