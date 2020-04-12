#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib,time,os


class SendEmail(object):

    def sendemail_QQ(self,report_path):
        # QQ邮件发送
        smtpserver = 'smtp.qq.com'
        sender = '123688711@qq.com'
        pwd = 'ywhfmrqegvhvbb'
        port = '465'
        receiver = ['546414168@qq.com', '19852659213@qq.com']
        # 实例化发送附件的对象
        msg = MIMEMultipart()
        msg['from'] = sender
        msg['to'] = ';'.join(receiver)
        msg['subject'] = 'web端自动化测试报告主题'
        with open(report_path, 'rb') as rp:
            web_mail_body = rp.read()
        '''正文'''
        body = MIMEText(web_mail_body, 'html', 'utf8')
        msg.attach(body)
        '''附件'''
        att = MIMEText(web_mail_body, 'base64', 'utf8')
        att['Connect-Disposition'] = \
            "attachment;filename = " \
            "'%s'" % report_path  # "%s"%report_path   直接拿取文件名
        msg.attach(att)
        '''发送邮件'''
        smpt = smtplib.SMTP_SSL(smtpserver, port)
        smpt.login(sender, pwd)
        smpt.sendmail(sender, receiver, msg.as_string())
        smpt.close()


    def sendemail_163(self,from_addr,password,mail_to,subject,path):
        '''
        163邮箱发送邮件
        :param from_addr: 发送邮件邮箱(163)
        :param password: 发送邮箱授权码
        :param mail_to: 接收邮件邮箱
        :param subject: 邮件主题
        :param path: 测试报告路径
        :return:
        '''
        mail_body = ''
        msg = MIMEMultipart()
        msg['Subject'] =subject
        msg['From'] = from_addr
        msg['to'] =mail_to
        msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        report_obj = open(path, 'rb')
        mail_body_value = report_obj.read()
        mail_body = mail_body_value
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(mail_body_value)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(r'C:\Users\Administrator\Desktop\xuesheng\report\xueshang.html'))
        msg.attach(part)
        report_obj.close()
        body = MIMEText(mail_body, _subtype="html", _charset='utf-8')
        msg.attach(body)
        smtp = smtplib.SMTP()
        server = smtplib.SMTP_SSL("smtp.163.com", 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, mail_to, msg.as_string())
        server.quit()

if __name__ == "__main__":
    S = SendEmail()
    # S.sendemail_QQ(r"D:\TestProject\PycharmProject\WebUnitTestingFramework\data\csv\login.csv")
    S.sendemail_163("186895752@163.com","8762345",
                    "1656645752@qq.com",
                    "wuwuwu",
                    r"D:\TestProject\PycharmProject\WebUnitTestingFramework\reports\web_test_reort_2016.06.06-16 30 13.html")