class Printer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print("调用_new_方法，创建对象，分配空间")
            cls.instance = object.__new__(cls)
        return cls.instance
