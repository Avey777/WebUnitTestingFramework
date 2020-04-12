#!/usr/bin/env python
#coding:utf8
import os
import pandas as pd
import pymssql
import pymysql
import sys
import sqlalchemy
from sqlalchemy import create_engine

class DataBase(object):
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    def __init__(self):
        pass
    '''读取同一数据库表Table1的数据写入到表Table2中'''
    def sql_read_and_insert(self,HostAdress,UserName,PassWord,Database,CharacterSet,Port,Table1,Table2):

        try:
            connect_sql = pymysql.connect(host=HostAdress,     #测试主机地址 'localhost'
                                          user=UserName,          #用户名    'root'
                                          password=PassWord,        #用户密码   None
                                          db=Database,          #数据库名   'testdb'
                                          port=Port,            #数据库端口
                                          charset=CharacterSet)       #字符集    'utf8'
        except pymysql.err.OperationalError as e:
            print('Error is ' + str(e))
            sys.exit()

        try:
            engine = create_engine('mysql+pymysql://'+UserName+':'+PassWord+'@'+HostAdress+':'+Port+'/'+Database)
        except sqlalchemy.exc.OperationalError as e:
            print('Error is ' + str(e))
            sys.exit()
        except sqlalchemy.exc.InternalError as e:
            print('Error is ' + str(e))
            sys.exit()

        try:
            #读取第一个表中的内容
            sql = 'select * from '+Table1
            df = pd.read_sql(sql, con=connect_sql)
        except pymysql.err.ProgrammingError as e:
            print('Error is ' + str(e))
            sys.exit()

        print(df.head())
        #将读取的第一个表中的内容写入到第二个表中
        df.to_sql(name=Table2, con=engine, if_exists='append', index=False)
        connect_sql.close()
        print('ok')

      # ''''
      #   插入初始数据sql语句
      #   insert into sum_case (type_id,type_name) values (1,'a'),(2,'b'),(3,'c')
      #   创建user1用户
      #   grant select, update,insert on test.* to 'user1'@'localhost' identified by '123456'
      #   test数据库里有两个表，建表语句如下：
      #   CREATE TABLE `sum_case` (
      #   `type_id` tinyint(2) DEFAULT NULL,
      #   `type_name` varchar(5) DEFAULT NULL,
      #    KEY `b` (`type_name`)
      #   ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
      #   '''


    '''试用方法-my try method'''
    '''读取 xx.sql 文件'''
    def sql_read_sqlfile(self, file_path, character_set):
        self.sql_file = open(file_path,  # xx.sql文件路径
                             encoding=character_set)  # xx.sql文件字符集（character_set）
        sql_scripts = self.sql_file.read()  # 仅读到sql语句，还没读取到数据
        return sql_scripts

    '''连接数据库'''
    def sql_connect(self, HostAdress, UserName, PassWord,Database,Port,CharacterSet, Connect_Satement):
        # 打开数据库连接
        db = pymysql.connect(host=HostAdress,  # 测试主机地址 'localhost'
                             user=UserName,  # 用户名    'root'
                             password=PassWord,  # 用户密码   None
                             db=Database,  # 数据库名   'testdb'
                             port=Port,  # 数据库端口
                             charset=CharacterSet)  # 字符集    'utf8'
        # 使用cursor()方法创建一个游标对象cursor
        cursor = db.cursor()
        # 使用excute()方法执行SQL查询
        # "SELECT VERSION()"
        sql = Connect_Satement
        cursor.excute(sql)
        # #使用fetchone()方法获取单条数据
        data = cursor.fetchone()
        print("Database version : %s "%data)
        # 关闭数据库连接
        db.close()

    '''数据库创建表'''
    def sql_create_table(self, HostAdress, UserName, PassWord, Database,Port,CharacterSet,Create_Statement):
        # 打开数据库连接
        db = pymysql.connect(host=HostAdress,  # 测试主机地址 'localhost'
                             user=UserName,  # 用户名    'root'
                             password=PassWord,  # 用户密码   None
                             db=Database,  # 数据库名   'testdb'
                             port=Port,  # 数据库端口
                             charset=CharacterSet)  # 字符集    'utf8'
        # 使用cursor()方法创建一个游标对象cursor
        cursor = db.cursor()
        # 使用excute()方法执行SQL,如果表存在则删除
        cursor.excute("DROP TABLE IF EXISTS EMPLOYEE")
        '''使用预处理语句创建表'''
        # """CREATE TABLE EMPLOYEE(
        #         FIRST_NAME CHAR(20) NOT NULL,
        #         LAST_NAME CHAR(20),
        #         AGE INT,
        #         SEX CHAR(1)
        #         INCOME FLOAT)"""
        sql = Create_Statement  # 创建数据库表的sql语句<parameter variable>
        # 执行sql语句
        cursor.execute(sql)
        # 关闭数据库连接
        db.close()

    '''数据库插入数据'''
    def sql_insert_data(self, HostAdress, UserName, PassWord, Database,Port,CharacterSet,Insert_Statement):

        # 打开数据库连接
        db = pymysql.connect(host=HostAdress,  # 测试主机地址 'localhost'
                              user=UserName,  # 用户名    'root'
                              password=PassWord,  # 用户密码   None
                              db=Database,  # 数据库名   'testdb'
                              port=Port,  # 数据库端口
                              charset=CharacterSet)  # 字符集    'utf8'
        # 使用cursor()方法创建一个游标对象cursor
        cursor = db.cursor()
        # SQL插入语句
        # "INSERT INTO EMPLOYEE( FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) \
        # VALUES('%s','%s','%d','%c','%d')" % ('Mac', 'Mohan', 20, 'M', 2000)
        sql = Insert_Statement  # sql插入语句<parameter variable>

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        # 关闭数据库连接
        db.close()
        return db

        # '''以下代码使用变量向SQL语句中传递参数'''
        # user_id = "test123"
        # password = "password"
        # con.excute('insert into Login values("%s","%s")'%(user_id,password))

    '''数据库查询操作'''
    def sql_custom_queries(self,HostAdress, UserName, PassWord,Database, Port,CharacterSet,Custom_Queries_Statement):
        # 打开数据库连接
        db = pymysql.connect(host=HostAdress,  # 测试主机地址 'localhost'
                             user=UserName,  # 用户名    'root'
                             password=PassWord,  # 用户密码   None
                             db=Database,  # 数据库名   'testdb'
                             port=Port,  # 数据库端口
                             charset=CharacterSet)  # 字符集    'utf8'

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        # "SELECT * FROM EMPLOYEE \
        # WHERE INCOME > '%d'" % (1000)
        sql = Custom_Queries_Statement
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            # 以自定义形式排列字段
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                      (fname, lname, age, sex, income))
        except:
            print("Error: unable to fetch data")
        # 关闭数据库连接
        db.close()

    '''数据库数据更新或删除记录'''
    def sql_update_or_del(self, HostAdress, UserName, PassWord,Database, Port,CharacterSet,Update_Del_Statement):
        # 打开数据库连接
        db = pymysql.connect(host=HostAdress,  # 测试主机地址 'localhost'
                             user=UserName,  # 用户名    'root'
                             password=PassWord,  # 用户密码   None
                             db=Database,  # 数据库名   'testdb'
                             port=Port,  # 数据库端口
                             charset=CharacterSet)  # 字符集    'utf8'

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 更新或删除语句
        # "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        # "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
        sql = Update_Del_Statement

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()


    #读取sql_server数据库
    def get_sql_server_data(self,file_path,file_reservation,character_set,address,username,password,db,charset):
        '''读取 xx.sql 文件'''
        self.sql_file = open(self.path + file_path,     #xx.sql文件路径
                        mode=file_reservation,           #xx.sql文件读取权限
                        encoding=character_set
                             )      #xx.sql文件字符集（character_set）
        sql_scripts = self.sql_file.read()  # 仅读到sql语句，还没读取到数据
        '''连接数据库,要先在cmd模式下用命令导入pymsql包，pip install pymysql'''
        self.sql_server_connect = pymssql.connect(
            host=address,  # 数据库所在机器的地址
            user=username,      #数据库登录用户名
            password=password,    #数据库登录密码（为空时可写：None）
            database=db,        # 数据库
            # port=port,          # 端口（不要加引号）  暂时不用
            charset=charset)       # 数据库字符集（防止读取数据库数据出现乱码）
        '''创建游标并读取数据库数据'''
        self.mssql_cursor = self.sql_server_connect.cursor()  # 创建游标，逐行读取数据
        self.mssql_cursor.execute(sql_scripts)  # 执行sql语句
        mssql_data = self.mssql_cursor.fetchall()  # 接收全部的返回结果行
        return mssql_data

if __name__ == '__main__':
    rw = DataBase()
    # rw.sql_read_and_insert("HostAdress",     #测试主机地址 'localhost'
    #                        "UserName",          #用户名    'root'
    #                        "PassWord",        #用户密码   None
    #                        "Datebase",          #数据库名   'testdb'
    #                        "Port",            #数据库端口
    #                        "CharacterSet",      #字符集    'utf8'
    #                        "Table1",
    #                        "Table2")
    # rw.sql_insert_data("localhost",
    #                              "root",
    #                              None,
    #                              "testdb",
    #                              3306,
    #                              "utf8",
    #                              "INSERT INTO employee (id,NAME,age) VALUES (i,'amie','23');")

    t = rw.get_sql_server_data("\demo\select.sql",
                              "r",
                              "utf-8",
                              '120.24.174.206',
                              'demo',
                              'demo',
                              'B2BTest',
                              'utf8')
    print(t)