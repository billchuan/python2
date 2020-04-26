# 4月26日学习
# 习题


# class Car:
#     def turn_left(self):
#         print("车向左转")
#
#     def turn_right(self):
#         print("车向右转")
#
#
# class WarCar(Car):
#     def fire(self):
#         print("战车开火")
#
#
# car = WarCar()
# car.turn_left()
# car.turn_right()
# car.fire()

# 继承的传递性
# class Animal:
#     def eat(self):
#         print("吃饭")
#
#     def drink(self):
#         print("喝水")
#
#     def run(self):
#         print("奔跑")
#
#     def sleep(self):
#         print("睡觉")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("汪汪叫")
#
#
# class XTDog(Dog):
#     def fly(self):
#         print("飞起")
#
#
# xt = XTDog()
# xt.eat()
# xt.drink()
# xt.sleep()
# xt.run()
# xt.bark()
# xt.fly()

# 对父类的拓展
class Dog:
    def bark(self):
        print("汪汪叫")


class XTDog(Dog):
    def fly(self):
        print("飞起")

    def bark(self):
        print("在天上汪汪叫")
        super().bark()
        print("￥￥%￥￥%&$&$&")


xt = XTDog()
xt.bark()
