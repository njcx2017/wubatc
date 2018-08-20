from scrapy.mail import MailSender
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class emailSender(object):
    def __init__(self):
	    user = 'njcx2017@163.com'
        password = '8324563cx'
        to = 'njcx2017@163.com'
        title = 'hahaha,scrapy do it'
        body = 'ffff'
		
		
    def sendEmail(self, to, subject, body):
	    user = 'njcx2017@sina.com'
        password = '8324563jin'
        to = 'njcx2017@163.com'
        title = 'hahaha,scrapy do it'
        body = '为什么不给我发呢，不是机器人哦'
	
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