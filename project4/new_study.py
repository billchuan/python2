# 6月15日上课学习
# 习题2


class Recycle(object):
    version = "佳能4410"

    def __init__(self, version):
        self.version = version
        print(version)

    def __new__(cls, *args, **kwargs):
        print("调用_new_方法，创建对象，分配空间")
        cls.version= super().__new__(cls)
        return cls.version


r = Recycle("佳能4411")
print(r)
