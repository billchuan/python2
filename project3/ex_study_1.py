# 5月18日五、六节课学习
class Fruit:
    def zhai(self):
        print("摘水果")

    def yunshu(self):
        print("运输水果")


class Banana(Fruit):
    def sell(self):
        print("卖水果")

    # 子类有与父类相同的方法
    # 1.(完全不一样)直接覆盖父类的方法
    # def zhai(self):
    #     print("从树上摘香蕉")
    # 2.(有一部分一样)子类中同名的方法，的实现方式中包含父类的实现方式
    def zhai(self):
        print("爬上树")
        super().zhai()
        print("爬下来")


Banana().zhai()

# 习题
# class Fruit:
#     def eat(self):
#         print("很好吃")
#
#
# class Apple(Fruit):
#     def info(self):
#         print("苹果很甜")
#         super().eat()
#         print("苹果很脆")
#
#
# Apple().info()
