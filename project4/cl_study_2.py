# 5月26日七、八节课学习
class Game(object):
    top_score = 0

    def __init__(self, name):
        self.play_name = name

    # 显示帮助信息
    @staticmethod
    def show_help():
        print("大吉大利，今晚吃鸡")

    # 设置最高分
    @classmethod
    def set_top_score(cls, score):
        cls.top_score = score

    # 显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("今日最高分:%d" % cls.top_score)

    # 实例方法
    def start_game(self):
        print("%s玩家欢迎进入游戏" % self.play_name)


# 查看帮助信息
Game.show_help()
# 设置历史最高分
Game.set_top_score(99)
# 打印历史最高分
Game.show_top_score()
# 开始游戏
# 创建对象
game = Game("王小五")
game.start_game()
# 习题1 类方法练习
# class Person(object):
#     category = "高级动物"
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def introduce(cls):
#         print(cls.category)
#
#
# Person.introduce()
