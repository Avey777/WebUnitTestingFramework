#!/usr/bin/env python
# coding:utf8
from time import sleep
import os
from basis.basis_driver import BasisDriver
from basis.log import Log

class BasisPage(object):
    PATH = os.path.abspath(os.path.dirname(os.getcwd()))
    def __init__(self,basis_driver:BasisDriver,basis_url):
        self.basis_driver = basis_driver
        self.basis_url = basis_url

    def open(self,url):
        self.basis_driver.navigate(self.basis_url + url)
        sleep(2)

    def log(self,info):
        log = Log(self.PATH  + '/logs')
        log.info(info)



