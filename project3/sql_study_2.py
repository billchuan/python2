# 4月28日学习
import pymysql

# 连接数据库
try:
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="db01", charset="GBK")
    print("连接成功")

    # 查询
    print("*********************************查询*********************************")
    cursor = conn.cursor()  # 创建一个游标对象，Python里的sql语句都要通过cursor来执行
    sql = "select * from person"
    cursor.execute(sql)  # 执行sql语句
    row = cursor.fetchone()  # 读取查询结果
    while row:  # 循环读取所有结果
        print("ID=%s,Name=%s,Age=%s" % (row[0], row[1], row[2]))  # 输出结果
        row = cursor.fetchone()
    print("*********************************修改*********************************")
    sql_2="update person set name='jack' where id='3'"
    print("修改成功")
    cursor.execute(sql_2)
    cursor.close()
    conn.close()
except Exception as err:
    print(err)


