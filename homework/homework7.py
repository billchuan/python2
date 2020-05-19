# 5月19日作业
class Father:
    def __init__(self):
        self.__money = 50000

    def get_money(self):
        print(self.__money)


class Son(Father):
    pass


s = Son()
s.get_money()
