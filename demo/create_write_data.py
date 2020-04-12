#!/usr/bin/env python3
# coding:utf8
import csv
from base.data_base import DataBase


class CreateWriteData(DataBase):

    def write_table_record(self,file_path ):
        dict = {'司徒玲': 0, '王大力': 0, '欧阳伊文': 0}
        '''打开csv文件'''
        file = open(file_path, mode="w",newline="")
        '''中文数据出现乱码处理方法:settings-editor-file encodings,设置GBK'''
        '''读取文件内容'''
        Writer = csv.writer(file)
        for i in range(10):
            for key in dict:
                Writer.writerow([key+"%d"%i,dict[key]+i])
        # 关闭文件
        file.close()

    # 更新或删除数据库数据
    def del_sql_dat(self):
        amie = DataBase()
        #删除sql语句
        sql_del = "DELETE FROM pw_active;"
        sql = sql_del
        #更新sql语句
        sql_update = ""
        sql = sql_update
        '''连接数据库'''
        amie.sql_update_or_del("192.168.1.111", #主机地址
                               "root",  #用户名
                               None,    #用户密码
                               "phpwind",   #数据路名
                               3306,    #数据库端口号
                               "utf8",  #字符集
                               sql) #sql语句
     #循环写入数据库数据
    def createsqldata(self,):
        # '''读取 xx.sql 文件'''
        # sql_file = open("..\demo\write.sql")
        # sql = sql_file.read()  # 仅读到sql语句，还没读取到数据
        amie = DataBase()
        num = range(int(input("请输入循环次数：")))
        for i in num:
            #sql语句
            sql_write = "INSERT INTO pw_active (id,title,uid) VALUES ('%d','amie%d','23');" %(i,i)
            '''连接数据库'''
            amie.sql_insert_data("192.168.1.111",  # 主机地址
                                   "root",  # 用户名
                                   None,  # 用户密码
                                   "phpwind",  # 数据路名
                                   3306,  # 数据库端口号
                                   "utf8",  # 字符集
                                 sql_write)  # sql语句
            print(i)

if __name__== "__main__":
    wr = CreateWriteData()
    # wr.createsqldata()
    wr.write_table_record(r"../demo/write.csv")

