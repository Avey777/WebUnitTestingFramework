import os

#获取当前的绝对路径
PATH_PROJECT = os.path.abspath(os.getcwd())
#获取当前路径的父级路径
path = os.path.abspath(os.path.dirname(os.getcwd()))
print(PATH_PROJECT)