import scrapy

from wubatc.items import WubatcItem
from scrapy.mail import MailSender
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import string
import time
#import re

class WubaSpider(scrapy.Spider):
    name = "wuba"
    allowed_domains = ["huxiu.com"]
    start_urls = [
            "https://www.huxiu.com/"
    ]
	
	
    def parse(self,response):

#        filename = response.url.split("/")[-2]
#        with open(filename,'wb') as f:
#            f.write(response.body)

        for sel in response.xpath('.//*[@id="index"]/div[1]/div[2]/div/div[2]/h2'):
            item = WubatcItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
#            item['desc'] = sel.xpath('text()').extract()
            yield item
'''         
    with open("E:\wubatc\wuba.json",'r',encoding='UTF-8') as load_f:
        load_dict = json.load(load_f)
        
        titt = []
        
        htm = []
        
        for tit in load_dict:
            html = tit['title']
            link = tit['link']
            json_str = json.dumps(html,ensure_ascii=False)
            json_st = json.dumps(link,ensure_ascii=False)
            htm.append('<a href='+json_st+'>'+json_str + '</a>' )
            cx = str(htm) 
    cc = cx.replace('=["','="http://www.huxiu.com').replace('"]>','">').replace('["','').replace('"]','').replace("', '","<br>").replace("['","").replace("']","")
    print(cc)

	
    user = 'njcx2017@sina.com'
    password = '8324563jin'
    to = 'njcx2017@163.com'
    title = str(time.ctime())
    body = cc
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = title
#    msg = MIMEText(body, 'html', 'utf-8')
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
       
'''
