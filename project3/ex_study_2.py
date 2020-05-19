# 5月19日五、六节课学习
# 1.在类的外部设置对象属性
# class Cat:
#     def eat(self):
#         print("%s喜欢吃鱼" % self.name)
#
#     def drink(self):
#         print("%s喜欢喝牛奶" % self.name)
#
#
# tom = Cat()
# tom.name = "汤姆"  # 在类的外部设置对象属性
# tom.eat()
# tom.drink()


# 2.在类的内部设置对象属性  在初始化的同时给对象的属性设置值
# class Cat:
#     def __init__(self, name, colour):  # 在创建该类的对象时会自动调用
#         self.name = name
#         self.colour = colour
#
#     def eat(self):
#         print("%s色的%s喜欢吃鱼" % (self.colour, self.name))
#
#
# tom = Cat("汤姆", "黑")
# tom.eat()
#
# jack = Cat("杰克", "白")
# jack.eat()

# 3.私有属性和私有方法
# java中私有属性 private int a = 1
# python中私有属性
class Animal:
    def __init__(self):
        self.name1 = "张三"  # 公有属性
        self.__name2 = "李四"  # 私有属性

    def test(self):  # 公有方法
        print(self.__name2)


# 在外部自己用
a = Animal()
print(a.name1)
# print(a.__name2) # 不能用
a.test()  # 调用公共方法
