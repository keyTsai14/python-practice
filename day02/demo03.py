import random

"""
循环

"""

# sum = 0
# for x in range(10):
#     sum+=11

# print(sum)

"""
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

"""

# sum = 0
# for x in range(0,101,1):
#     sum+=x

# print(sum)


"""
while循环


"""
# answer = random.randint(1, 100)
# counter = 0
# sum = 0
# while counter<10:
#     sum+=counter
#     counter+=1

# print(sum)

"""
九九乘法口诀

"""

# for i in range(1,10):
#     for j in range(1,10):
#         print('%d * %d = %d' %(i,j,i*j))
#     print()


"""
练习1：输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。

"""

# from math import sqrt

# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# print(end)
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)


"""
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

"""
# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较小的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break


"""
打印三角形
    
    
"""

row = int(input('请输入行数：'))
for i in range(row):
    for j in range(i+1):
        print('*',end='')
    print()

print('==================')
for i in range(row):
    for j in range(row):
        if (j<(row-i-1)):
            print(' ',end='')
        else:
            print('*',end='')    
    print()

print('==================')
for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for j in range(2*i+1):        
        print('*',end='')            
    print()    