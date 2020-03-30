# 3月30日学习代码

# 打印万年历


def is_leap(y):
    """判断闰年"""
    result = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    return result


def max_days(y, m):
    """计算某年某月有多少天"""
    # 1、正常天数
    days = 30
    # 2、31天的情况
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        days = 31
    # 3、闰月情况
    if m == 2:
        if is_leap(y):
            days = 29
        else:
            days = 28
    return days


def count_days(y, m, d):
    """计算某年某月某日是该年的第几天"""
    days = d
    if m >= 2:
        days += 31
    if m >= 3:
        if is_leap(y):
            days += 29
        else:
            days += 28
    if m >= 4:
        days += 31
    if m >= 5:
        days += 30
    if m >= 6:
        days += 31
    if m >= 7:
        days += 30
    if m >= 8:
        days += 31
    if m >= 9:
        days += 31
    if m >= 10:
        days += 30
    if m >= 11:
        days += 31
    if m >= 12:
        days += 30
    return days


