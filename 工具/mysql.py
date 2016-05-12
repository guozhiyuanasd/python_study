
# -*- coding: utf-8 -*-
import pymysql

class MysqlUtils:
    def __init__(self,host,username,password,dbName,port=3306,charset="utf8"):
        self.host=host
        self.username=username
        self.password=password
        self.dbName=dbName
        self.port=port
        self.charset=charset
        conn=pymysql.connect(host=host,user=username,passwd=password,db=dbName,port=port,charset=charset)
        self.connection=conn

    def queryForMap(self,sql,params):
          try:
              if params=="" or params is None:
                  params=()
              conn=self.connection
              with conn.cursor() as cursor:
                   cursor.execute(sql,params)
                   result = cursor.fetchall()
              returnData=[]
              for i,data in enumerate(result):
                   rs={};
                   for field_desc in cursor.description:
                        rs[field_desc[0]]=data[i]
                   returnData.append(rs)
              return returnData
          except Exception as e:
              print("异常："+e)
          finally:
              cursor.close()#关闭游标
              #conn.close()#释放数据库资源
    def excuteSql(self,sql,params):
          try:
              if params=="" or params is None:
                  params=()
              conn=self.connection
              with conn.cursor() as cursor:
                  cursor=conn.cursor()
                  cursor.execute(sql,params)
                  conn.commit();
                  return result

          except Exception as e:
              print("异常："+e)
          finally:
              cursor.close()#关闭游标
              #conn.close()#释放数据库资源
    def closeConnection(self):
          self.connection.close();


mysql=MysqlUtils("127.0.0.1","root","123456","test")
result=mysql.queryForMap("select `id`,`name`,`age` from person",())
for r in result:
    print(r)
mysql.excuteSql("update person set name='zzzz' where id =%s",("1"))
