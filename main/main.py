#!/usr/bin/env python
# coding:utf8
from runner.test_runner import TestRunner


class Main(object):
    def start_web_test(self):
        test_runner = TestRunner()
        test_runner.runner()

if __name__ == '__main__':
    main = Main()
    main.start_web_test()
