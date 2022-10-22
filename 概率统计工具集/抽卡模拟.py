from random import random

'''
局部变量
    pay：总抽卡次数
    p=普通掉率
    # p_s=补偿掉率(本例=1，用不上)
    times=保底次数
    
    n:记录保底内抽卡次数
    
    i：记录抽到金卡次数
模拟抽卡次数可以用
    1.for...range
    2.列表生成式
    3.map+lambda
'''


def card_draw(pay=100000000, p=0.01, times=10):
    i = 0
    n = 0

    for x in range(pay):
        n += 1
# 写法一
#         if p >= random():
#             i += 1
#             n = 0
#         elif (n != 1) and ((n - 1) % times) == 0:
#
#             '''
#         上一行代码很容易错写成如下形式
#         elif n % times == 0:
#         错误原因在于 保底次数为3指的是抽4次保底1次，而不是抽3次保底1次
#         补充 (n!=1) 是为了避免第一次循环 n=1 导致后续 elif 语句判断始终可以通过
#         '''
#             i += 1
#             n = 0
# 写法二
        ran = random()
        if p >= ran or (p < ran and (n != 1) and ((n - 1) % times) == 0):
            i += 1
            n = 0
    return [i, i / pay]


print(card_draw(p=0.25, times=3))
