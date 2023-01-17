"""
date:2023-01-17
time:20:22
author:bipeng
adderss:henan luohe
"""


def f():
    try:
        print(1)
        return 2
    finally:
        print(3)
        return 4


print(f())

"""
结果为1,3,4
说明无论try里执行什么，即使是return，也会调用finally的。

"""
#**********************************************************************************

def f():
    try:
        print(1)
        return 2
    finally:
        print(3)
        #return 4

print(f())

"""
结果为1,3,4
对比上个结果，说明try的返回值被finally的返回值覆盖了，或许是因为一个函数只能有一个返回值，以最后一个结果为准

"""

#**********************************************************************************

def f():
    try:
        print(1)
        return 2
    except:
        return 3
    else:
        print(4)
        return 5
    finally:
        print(6)
        #return 0

print(f())

"""
结果为1，6,2
你觉得，没有异常else会执行吗？

如你所料，并没有执行。

结果为 1 0 1

说明try里面运行完之后return，阻挡了else的执行，但是并没有影响finally的执行。
"""


#**********************************************************************************
"""
借用Vamer文章的两句话：

“如果try中没有异常，那么except部分将跳过，执行else中的语句。（前提是try里没有返回值）

finally是无论是否有异常，最后都要做的一些事情。”（无论try里是否有返回值）

这里补充一句，在含有return的情况下，并不会阻碍finally的执行。（但是会阻碍else）


自己的总结：

不要在try else里写返回值。如果没有finally，就写在最后，或者只写在finally里。

try except else里都是做某事   而不是处理返回

"""




#**********************************一些小测试************************************************




def test_finally_return1():
    try:
        print(1)
        return 2
    finally:
        print(3)
        return 4


def test_finally_return2():
    try:
        print(1)
        return 2
    finally:
        print(3)
        #return 4


def test_else_finally1():
    try:
        print(1)
        return 2
    except:
        return 3
    else:
        print(4)
        return 5
    finally:
        print(6)
        #return 7

def test_else_finally2():
    try:
        print(1)
        return 2
    except:
        return 3
    else:
        print(4)
        #return 5
    finally:
        print(5)
        return 6


def test_else_finally3():
    try:
        print(1)
        #return 2
    except:
        print(3)
        #return 4
    else:
        print(5)
        #return 6
    finally:
        print(7)
        return 8

def test_else_return1():
    try:
        print(1)
        return 2
    except:
        return 3
    else:
        print(4)
        return 5
    # finally:
    #     print(6)
        #return 7
print("test3")

def test_else_return2():
    try:
        print(1)
        #return 2
    except:
        return 3
    else:
        print(4)
        return 5
    finally:
        print(6)
        return 7


if __name__ == '__main__':
    print('测试1')
    print(test_finally_return1())
    print('测试2')
    print(test_finally_return2())
    print('测试3')
    print(test_else_finally1())
    print('测试4')
    print(test_else_finally2())
    print('测试5')
    print(test_else_finally3())

    print('测试6')
    print(test_else_return1())

    print('测试7')
    print(test_else_return2())
    
    print("test")
    print("test1")
