# 4月27日学习
import pymysql

try:
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="db01", charset="GBK")
    print("连接成功")
except Exception as err:
    print(err)
# 查询
cusor = conn.cursor()  # 创建一个游标对象，Python里的sql语句都要通过cursor来执行
sql = "select * from person"
cusor.execute(sql)  # 执行sql语句
row = cusor.fetchone()  # 读取查询结果
while row:  # 循环读取所有结果
    print("ID=%s,Name=%s,Age=%s" % (row[0], row[1], row[2]))  # 输出结果
    row = cusor.fetchone()
cusor.close()
conn.close()
