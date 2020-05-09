# 5月9日作业
import pymysql

try:
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           passwd="root",
                           db="WangHaiChuan",
                           charset="GBK")
    print("连接成功")
except Exception as err:
    print(err)
