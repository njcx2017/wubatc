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
        self.collection.insert(dict(item))
        return item






'''
    # 调用 scrapy 提供的 json exporter 导出 json 文件
    def __init__(self):
        self.file = open('wuba.json', 'wb')
        # 初始化 exporter 实例，执行输出的文件和编码
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        # 开启倒数
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
'''
		
 		
		
		
		
'''
    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
		
'''    
