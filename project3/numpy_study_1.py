# 5月12日七、八节课

import numpy as np

# a = np.linspace(0, 10, 5)  # 创建等差数组，在0-10之间分成5份
# print("a=", a)


list1 = [1, 2, 3, 4, 5]

a0 = np.array(list1)  # 将列表转换成数组
print(a0)
a1 = np.array(list1, dtype=np.float)
print("a1=", a1)

# 创建有5个元素的一维数组
a2 = np.array(range(1, 6))
print("a2=", a2)

# 创建等差数组
a3 = np.linspace(1, 10, 5)
print("a3=", a3)

# 创建二维数组
a4 = np.zeros([3, 3])
print("a4=", a4)

a5 = np.ones([3, 3])
print("a5=", a5)

a6 = np.identity(3)
print("a6=", a6)
