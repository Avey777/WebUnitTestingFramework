#!/usr/bin/env python3
# coding:utf8
from basis.basis_page import BasisPage
from  config.elelocinfo import *

class LoginPage(BasisPage):

    def login(self, username,password):
        driver = self.basis_driver

        self.log("输入登录用户名")
        driver.type(username_xpath,username)
        self.log("输入登录密码")
        driver.type(password_id,password)
        self.log("点击登录按钮")
        driver.click(login_btn_xpath)
        driver.sleep(3)
        

    def login_inherit(self,data):

        driver = self.basis_driver
        self.log("输入登录用户名")
        driver.type_clear(username_xpath,data['username'])
        self.log("输入登录密码")
        driver.type_clear(password_id, data['password'])
        self.log("点击登录按钮")
        driver.click(login_btn_xpath)
        driver.sleep(3)


        if data['casetype'] == 'True':
            self.log("执行登录成功用例")

            exist = driver.isElementExist(logout_xpath)
            if exist == True:
                self.log("获取登陆成功的断言文本")
                self.TURE_TEXT = driver.get_title()
                print("登陆成功的title：" + self.TURE_TEXT)
                self.log("点击退出登录按钮")
                driver.click(logout_xpath)
                driver.sleep(1)
            if exist == False:
                self.log('判断接受alert')
                driver.alert_exist_accept()

        if data['casetype'] == 'False':
            self.log("执行登录失败用例")
            try:
                self.log('判断接受alert')
                driver.alert_exist_accept()
            except:
                print('ALERT不存在')
            exist = driver.isElementExist(exist_id)
            if exist == True:
                self.log("获取登录失败的断言文本")
                self.FAIL_TEXT = driver.get_text(account_text_xpath)
                print(self.FAIL_TEXT)
                driver.sleep(1)
                pass
            if exist == False:
                print("执行错误用例退出登陆")
                self.log("点击退出登录按钮")
                driver.click(logout_xpath)
                driver.sleep(2)




