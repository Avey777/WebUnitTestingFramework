#!/usr/bin/env python
# coding:utf8
import smtplib
import time
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from basis.html_test_runner import HtmlTestRunner


class TestRunner(object):
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    def runner(self):
        '''创建测试套件和生成测试报告'''
        '''实例化TestSuit类'''
        test_suite= unittest.TestSuite()

        # # 添加测试用例测试套件test_suite
        # # 测试添加运行单个用例
        # test_suite.addTest(WebTestLogin('test_login'))
        # test_suite.addTest(WebTestLogin('test_sql_login'))
        #
        '''测试添加运行多个用例'''
        cases_path = 'cases'
        discover = unittest.defaultTestLoader.discover(cases_path,
                                            pattern='web_test*.py',
                                           top_level_dir=None)
        # print('discover:',discover)
        for testsuite in discover:
            for test_case in testsuite:
                test_suite.addTests(test_case)
        print('test_suite:',test_suite)

        # 创建测试报告（没有会自动生成）时间戳
        # report_path = 'web_test_report_%s.html'%time.time()
        '''创建测试报告（没有会自动生成）时间戳转换为本地时间格式形式'''
        report_path= self.path + '/reports/web_test_reort_%s.html'\
                     %time.strftime('%Y.%m.%d-%H %M %S',time.localtime())

        report_file = open(report_path,'wb') #（binary write）以二级制写入
        test_runner = HtmlTestRunner(report_file,
                                     title='WEB自动化测试报告',
                                     description='测试详情')

        #运行测试用例
        test_runner.run(test_suite)
        report_file.close()





