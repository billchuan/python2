# 5月19日七、八节课学习


class A:

    def swim(self):
        print("会游泳")

    def jump(self):
        print("会跳")

    def fly(self):
        print("A.....................会飞")


class B:
    def run(self):
        print("会奔跑")

    def climb(self):
        print("会爬树")

    def fly(self):
        print("B.....................会飞")


class C(A, B):
    pass


c = C()
print(C.__mro__)
c.fly()
