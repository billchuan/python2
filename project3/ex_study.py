# 5月18日五、六节课学习


# 习题
class Fruit:
    def eat(self):
        print("很好吃")


class Apple(Fruit):
    def info(self):
        print("苹果很甜")
        super().eat()
        print("苹果很脆")


Apple().info()
