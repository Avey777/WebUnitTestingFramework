#!/usr/bin/env python
# coding:utf8
import logging
import os
import time

class Log(object):

	def __init__(self,log_path):
		# log_path：日志存放路径
		# 文件命名
		self.logname = os.path.join(log_path,'%s.log' %time.strftime('%Y-%m-%d '))
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		# 日志输出格式
		self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-'
										   '%(levelname)s:%(message)s')
	def _console(self,level,message):
		# 创建一个FileHandler，用于写到本地
		fh = logging.FileHandler(self.logname,'a',encoding='utf8')
		fh.setLevel(logging.DEBUG)
		fh.setFormatter(self.formatter)
		self.logger.addHandler(fh)
		# 创建一个SteamHandler,用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		ch.setFormatter(self.formatter)
		self.logger.addHandler(ch)
		if level == 'info':
			self.logger.info(message)
		elif level == 'debug':
			self.logger.debug(message)
		elif level == 'warning':
			self.logger.warning(message)
		elif level == 'error':
			self.logger.error(message)
		else:
			self.logger.info('请输入正确的level！')
		# 这两行代码为了避免日志输出重复
		self.logger.removeHandler(ch)
		self.logger.removeHandler(fh)
		# 关闭打开的文件
		fh.close()

	def debug(self,message):
		self._console('debug',message)
	def info(self,message):
		self._console('info',message)
	def warning(self,message):
		self._console('warning',message)
	def error(self,message):
		self._console('error',message)

if __name__ == '__main__':
	# log = Log('logs')
	log = Log('../logs')
	log.info('开始测试')
	log.info('输入密码')
	log.warning('结束测试')
	log.error('报错')