import scrapy

from wubatc.items import WubatcItem
from scrapy.mail import MailSender
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import string
import time
import pymongo
from scrapy.conf import settings

class WubaSpider(scrapy.Spider):
    name = "wuba"
    allowed_domains = ["huxiu.com"]
    start_urls = [
            "https://www.huxiu.com/"
    ]
	
	
    def parse(self,response):
		
        for big in response.xpath('.//*[@id="index"]/div[1]/div[1]/div[1]'):
		
            item = WubatcItem()
            item['title'] = big.xpath('a/div[2]/h1/text()').extract()
            item['link'] = big.xpath('a/@href').extract()
            item['datetime'] = time.ctime()
            yield item
			
        for big2 in response.xpath('.//*[@id="index"]/div[1]/div[1]/div/a[2]'):
		
            item = WubatcItem()		
            item['title'] = big2.xpath('div/h2/text()').extract()
            item['link'] = big2.xpath('@href').extract()
            item['datetime'] = time.ctime()
            if item !='':
                yield item


        for sel in response.xpath('.//*[@id="index"]/div[1]/div[2]/div/div/h2'):
            item = WubatcItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['datetime'] = time.ctime()
            yield item
			
    def __init__(self):
        connection = pymongo.MongoClient(settings.get('MONGODB_SERVER'),settings.get('MONGODB_PORT'))
        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]
		
        maildata = self.collection.find({},{"title":1,"link":1,"_id":0}).limit(30)
        htm = []
        for content in maildata:
            html = content['title']
            link = content['link']
            json_str = json.dumps(html,ensure_ascii=False)
            json_st = json.dumps(link,ensure_ascii=False)			
            htm.append('<a href='+json_st+'>'+json_str + '</a>' )
        cx = str(htm)        
        cc = cx.replace('=["','="http://www.huxiu.com').replace('"]>','">').replace('["','').replace('"]','').replace("', '","<br>").replace("['","").replace("']","")
        			
					
        user = 'njcx2017@sina.com'
        password = '8324563jin'
        to = 'njcx2017@163.com'
        title = str(time.ctime())
        body = cc
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = to
        msg['Subject'] = title
        msg.attach(MIMEText(body, 'html', 'utf-8')) 

        try:
            mailServer = smtplib.SMTP('smtp.sina.com', 25)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login(user, password)
            mailServer.sendmail(user, to, msg.as_string())
            mailServer.close()
            print("邮件发了哦")
        except smtplib.SMTPException as e:
            print(e)        
			