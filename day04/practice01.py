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



# import demo01 as d1

# d1.foo()



"""练习"""

#################################################实现计算求最大公约数和最小公倍数的函数。#################################################

def gcd(x,y):
    """最大公约数"""
    (x,y) = (y,x) if x>y else (x,y)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x,y):
    """求最小公倍数"""
    return x*y // gcd(x,y)



#################################################【实现判断一个数是不是回文数的函数。】#################################################

def is_palindrome(num):
    """判断一个数是否回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num



#############【实现判断一个数是不是素数的函数。】###################

def is_prime(num):
    """判断一个数是否素数"""
    for factor in range(2,int(num**0.5)+1):
        if num % factor == 0:
            return False
        return True if num != 1 else False


#############【写一个程序判断输入的正整数是不是回文素数。】###################

# if __name__ == '__main__':
#     num = int(input('请输入正整数:'))
#     if is_palindrome(num) and is_prime(num):
#         print('%d是回文素数' % num)



"""
变量的作用域
最后，我们来讨论一下Python中有关变量作用域的问题。
"""

def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()


"""
上面的代码能够顺利的执行并且打印出100、hello和True，
但我们注意到了，在bar函数的内部并没有定义a和b两个变量，
那么a和b是从哪里来的。我们在上面代码的if分支中定义了一个变量a，
这是一个全局变量（global variable），属于全局作用域，
因为它没有定义在任何一个函数中。在上面的foo函数中我们定义了变量b，
这是一个定义在函数中的局部变量（local variable），属于局部作用域，在foo函数的外部并不能访问到它；
但对于foo函数内部的bar函数来说，变量b属于嵌套作用域，在bar函数中我们是可以访问到它的。bar函数中的变量c属于局部作用域，
在bar函数之外是无法访问的。事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，
前三者我们在上面的代码中已经看到了，所谓的“内置作用域”就是Python内置的那些标识符，我们之前用过的input、print、int等都属于内置作用域。


"""    



def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200


"""
global关键字来指示foo函数中的变量a来自于全局作用域

实际开发中，我们应该尽量减少对全局变量的使用，因为全局变量的作用域和影响过于广泛，
可能会发生意料之外的修改和使用，除此之外全局变量比局部变量拥有更长的生命周期，可能导致对象占用的内存长时间无法被垃圾回收

"""    