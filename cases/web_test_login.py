#!/usr/bin/env python
# coding:utf8
import csv
import unittest
import time

import os

from basis.basis_driver import BasisBrowser, BasisDriver
from base.windows_text import open_tkinter
from pages.login_page import LoginPage


class WebTestLogin(unittest.TestCase,LoginPage):

    path = os.path.abspath(os.path.dirname(os.getcwd()))
    Adress = '120.24.124.216'
    BASIS_BROWSER = BasisBrowser.Edge
    base_url = "www.xxxxxx/account/login?"

    #使用basis_driver
    def setUp(self):
        pass
        # self.base_url = "http://" + self.Adress + ":8080/bi"
        self.driver = BasisDriver(self.BASIS_BROWSER)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.LOGINPAGE = LoginPage(self.driver,self.base_url)   #实例化LoginPage作为局部变量时使用
        self.LOGINPAGE.open("")
    #     open_tkinter("/data/photo/huozhan.gif",
    #                              '\n -----------模拟用户登陆测试-----------\n',
    #                              '''
    # 1、正确的用户名密码，登陆
    # 2、错误的用户名，登陆
    # 3、错误的密码，登陆
    # 4、用户名为空，密码输入数据库存在的信息，登陆
    # 5、密码为空，用户名输入数据库存在的信息，登陆
    # 6、输入特殊字符(含空值)，登录
    # 7、输入略超过字符限制的用户名、密码，登录
    # 8、输入略少于字符限制的用户名、密码，登录
    #
    #                              ''')
    def tearDown(self):
        self.driver.quit_browser()
        pass

    '''使用csv文件传参'''
    def test_login_page(self):

        self.driver.xlsx_csv("/data/case.xlsx", 'login', "/data/csv/login.csv")
        self.log("打开csv文件")
        self.csv_file = open(self.path + r'/data/csv/login.csv',  # csv文件路径
                             mode='r',  # 获得文件权限
                             encoding='utf8')  # 字符集

        self.log("读取csv文件")
        csv_data = csv.reader(self.csv_file)

        self.log("跳过第一行数据")
        is_header = True
        for line in csv_data:
            if is_header:
                is_header = False
                continue    #跳出本次循环

            self.log('csv文件数据生成字典')
            data = {'number':line[0],
                    'username':line[1],
                    'password':line[2],
                    'casetype':line[3]}

            self.log("实例化LoginPage作为局部变量")
            LOGINPAGE = LoginPage(self.driver,self.base_url)
            self.log("调用对象LoginPage中的方法login_inherit并传递(data dict)参数")
            LOGINPAGE.login_inherit(data)
            try:
                self.log("开始执行断言")
                if data['casetype'] == 'True':
                    self.log("获取断言文本1")
                    TITLE = LOGINPAGE.title
                    self.driver.assertion_log(TITLE,
                                              "供应链",
                                              "\nTrue断言失败:" + data['number']+
                                              "\n断言生成时间："+
                                              (time.strftime("%Y/%m/%d-%H:%M:%S",time.localtime()))+"\n",
                                              r'/screenshots',
                                              r'/logs/logs_assert/assert_true.txt')


                if data['casetype'] == 'False':
                    self.log("获取断言文本2")
                    text = LOGINPAGE.FAIL_TEXT
                    self.log("执行登录失败断言")

                    self.driver.assertion_log(text,
                                              " 账户登录 ",
                                              "\nFalse断言失败:" +
                                              data['number']+"\n断言生成时间："+
                                              (time.strftime("%Y/%m/%d-%H:%M:%S",time.localtime()))+"\n",
                                              r'/screenshots',
                                              r'/logs/logs_assert/assert_false.txt')
            except:
                print('跳过断言:'+ data['number'])

        self.log("关闭csv文件")
        self.csv_file.close()

    # '''使用数据库数据传参'''
    # def test_sql_login(self):
    #
    #     sql_data = self.driver.get_sql_data(
    #         r'..\WEB_TEST\data\login_mysql.sql',    #xx.sql文件路径(file_path)
    #         'r',        #xx.sql文件读取权限(file_reservation)
    #         'utf8',     #xx.sql文件字符集（character_set）
    #         self.Adress,    # 数据库所在机器的地址（adress）
    #         'root',         #数据库用户名(username)
    #         None,           #数据库密码（password为空时可写：None）
    #         'rs_report',    # 数据库(database)
    #         3306,            # 端口（port不要加引号）
    #         'utf8')         # 数据库字符集（charset防止读取数据库数据出现乱码）
    #     try:
    #         for line in sql_data:
    #             data = {'username': line[0],
    #                     'password':123456,
    #                     'casetype':line[2]}
    #             # self.log("实例化LoginPage作为局部变量")
    #             LOGINPAGE = LoginPage(self.driver,self.base_url)
    #             # self.log("调用对象LoginPage中的方法login_inherit并传递(data dict)参数")
    #             LOGINPAGE.login_inherit(data)
    #
    #             # self.log("开始执行断言")
    #             if data['casetype'] == 'True':
    #                 self.log("获取断言文本")
    #                 text = LOGINPAGE.TURE_TEXT
    #                 self.log("执行登录成功断言")
    #                 self.assertEqual('睿思BI - 系统介绍',text,'登录失败')
    #             if data['casetype'] == 'False':
    #                 self.log("获取断言文本")
    #                 text = LOGINPAGE.FAIL_TEXT
    #                 self.log("执行登录失败断言")
    #                 self.assertEqual('账号不存在，请确认账号是否输入正确！',text,'断言失败')
    #     except:
    #         # self.log("抓取断言失败屏幕截图")
    #         self.driver.get_screenshot('screenshots')
    #     finally:
    #         # self.log("关闭数据库")
    #         self.driver.close_sql()

if __name__ == '__main__':
    unittest.main()

