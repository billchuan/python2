import pymysql


class StudentDB:
    # 创建
    def create_table(self):
        sql_str = """
        create table student(
        id int primary key,
        name varchar(20),
        banji int,
        age int
        )
        """
        try:
            self.conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="db01",
                                        charset="GBK")
            print("连接成功")
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql_str)
        except Exception as err:
            print(err)

    # 添加
    def insert_data(self, id, name, banji, age):
        try:
            sql = "insert into student(id,name,banji,age) values (%s,%s,%s,%s)"
            print(sql)
            self.cursor.execute(sql, (id, name, banji, age))
            print("插入成功")
        except Exception as err:
            print("插入失败")
            print(err)

    # 导出
    def export(self):
        try:
            file_obj = open("C:\\Users\\Lenovo\\Desktop\\whc.txt", "a")
            self.cursor.execute("select *from student")
            file_obj.write("*"*40+"\n")
            file_obj.write("序号\t姓名\t班级\t年龄\n")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                file_obj.write(str(row[0]) + "\t" + row[1] + "\t" + str(row[2]) + "\t" + str(row[3]) + "\n")
            file_obj.write("*"*40)
            file_obj.close()
            print("成绩导出完毕")
        except Exception as err:
            print(err)

    # 关闭数据库
    def close_conn(self):
        self.conn.commit()
        self.conn.close()


"""主程序"""
student = StudentDB()
student.create_table()
student.insert_data(1, "zhangsan", 10, 20)
student.insert_data(2, "lisi", 10, 25)
student.insert_data(3, "wangwu", 10, 21)
student.export()
student.close_conn()
