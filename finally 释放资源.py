import os, sys

# python推出的方法
try:
    quit()  # 相当于raise SystemExit,可以被捕捉到
    exit()  # 相当于raise SystemExit，可以被捕捉到
    sys.exit()  # 相当于raise SystemExit，可以被捕捉到

    os._exit(1) #是比较底层的一个推出命令，不能被python捕捉到

except SystemExit as e:
    print(e)

finally:
    print("finally")

import atexit


@atexit.unregister
@atexit.register
def test():
    print('test')


def func():
    print('func2')


atexit.register(func)
atexit.register(func)
atexit.unregister(func)

"""
用atexit.register()注册一个函数，当程序执行完时，会自动调用func()函数
用atexit.unregister()取消注册。当注册多次。只需一次unregister()即可取消多次的register
"""

atexit._run_exitfuncs()  # 提前运行注册的函数，不用等到程序结束
atexit._clear()  # 清楚除所有注册的函数
print(atexit._ncallbacks())  # 获得atexit注册函数的数量


# atexit.unregister判断两个函数相等用的是==而不是is


class MyClass:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return True

    def __call__(self, *args, **kwargs):
        print("exciting call")


f1 = MyClass('f1')
atexit.register(f1)
f2 = MyClass('f2')
atexit.register(f2)

atexit.unregister(f1)

"""
只需要unregister()一次即可取消f1和f2的注册。因为unregister()通过__eq__判断两个是同一个函数对象。
"""
