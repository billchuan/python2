# 类属性
class Student(object):
    student_count = 0

    def __init__(self, student_name):
        self.student_name = student_name
        Student.student_count += 1

    @staticmethod
    def welcome_info():
        print("欢迎访问学生管理系统")

    @classmethod
    def show_student_count(cls):
        print("学生总数:%d" % cls.student_count)

    def login_system(self):
        print("%s同学开始进入管理系统" % self.student_name)


# 主程序
s1 = Student("王海川")
s2 = Student("李四")
s3 = Student("王五")
s4 = Student("张三")
Student.welcome_info()
Student.show_student_count()
s1.login_system()
