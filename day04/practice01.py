"""
函数和模块的使用

"""

# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1,m+1):
#     fm*=num

# fn = 1
# for num in range(1,n+1):
#     fn*=num

# fm_n = 1
# for num in range(1,m-n+1):
#     fm_n*=num
# print('fm = %d' % fm)
# print('fn = %d' % fn)
# print('fm_n = %d' % fm_n)
# print(fm // fn // fm_n)



def fac(num):
    # 阶乘
    result = 1
    for n in range(1,num+1):
        result*=n
    return result


# m = int(input('m = '))
# n = int(input('n = '))
# print(fac(m) // fac(n) // fac(m-n))



"""
函数是绝大多数编程语言中都支持的一个代码的"构建块"，但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，其中一个显著的区别就是Python对函数参数的处理。
在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持函数的重载，
"""


from random import randint

def roll_dice(n=2):
    # 摇骰子
    total = 0
    for _ in range(n):
        total+= randint(1,6)
    return total

# def add(a=0,b=0,c=0):
#     return a+b+c

# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))


def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# 在调用add函数时可以传入0个或多个参数
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 3, 5, 7, 9))


# import module1 as m1
# import module2 as m2

# m1.foo()

# m2.foo()



import module3


# m3.ccc()
# m3.foo()
# m3.bar()