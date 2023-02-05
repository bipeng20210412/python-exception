from typing import no_type_check, no_type_check_decorator, Annotated

# 出现异常过于宽泛的提示。在 try 语句前加入 # noinspection PyBroadException 即可
# noinspection PyBroadException
try:
    1 + 1
except Exception:  # 没有写具体的异常，就会异常过于宽泛
    print("hello,world")


# **********************************************************************************
class MyException(Exception):  # 自定义异常
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MyException("My exception")

except MyException as e:  # 可以写单个异常
    e.__note__ = "hello,world"
    print(e)
except (ZeroDivisionError, ArithmeticError) as e:  # 可以把几个异常写成元组，出现任何一个异常，就可以捕获
    print(e)
else:
    print("no exception")
finally:
    print("finally")

# **********************************************************************************

# ExceptionGroup可以把多个异常合成一个组合一起raise,然后利用split和subgroup，except*可以分批截取各个异常
g_1 = ExceptionGroup("g", [ValueError("value error"), TypeError("type error", 2), IndexError("index error")])

print(g_1.split(lambda e: isinstance(e, ValueError))[0])
"""
split函数将ExceptionGroup分为符合条件的和不符合条件的  
(ExceptionGroup('g', [ValueError('value error')]), ExceptionGroup('g', [TypeError('type error', 2), IndexError'indexerror')])) 

"""

print(g_1.subgroup(lambda e: isinstance(e, IndexError)).message)
print(g_1.subgroup(lambda e: isinstance(e, IndexError)).args)
"""
subgroup将函数将ExceptionGroup符合条件的异常给筛选出来
结果为g (1 sub-exception)
  
"""

try:
    raise g_1
except* (ValueError, TypeError) as e:  # 同时获取异常组合
    print(e.message)
    print(e.args[1])  # 结果为[ValueError('value error'), TypeError('type error', 2)]
    print(e.args[1][1])  # 结果为('type error', 2)

except* IndexError as e:
    print(e.message)
    print(e.args[1])  # 结果为[IndexError('index error')]
    print(e.args[1][0])  # 结果为index error

else:
    print("no exception")

finally:
    print("finally")

"""


"""

# **********************************************************************************


g_2 = ExceptionGroup("g_2", [IndexError("index error"), IndexError("index error_1"), MyException(
    "My exception")])  #
# 两种同类型的异常也可以捕获


try:
    raise g_2
except* IndexError as e:

    print(e.message)
    print(e.args[1])  # [IndexError('index error'), IndexError('index error_1')]
    print(e.args[1][0], e.args[1][1])  # index error index error_1

except* MyException as e:
    print(e)

"""
 1:对于ExceptionGroup中所有匹配的异常，每个 except* 子句最多执行一次。每个异常要么由第一个匹配其类型的子句处理，要么在最后重新抛出。
 2:except 能捕获 BaseExceptionGroup 和 ExceptionGroup，但 except* 不能（这个语法是模糊的，被禁止了）。
  except ValueError:  // OK, 捕获裸异常
  except ExceptionGroup:  // OK, 捕获异常组
  except* ValueError:  // OK, 捕获裸异常 & 异常组
  except* ExceptionGroup: // 错误！
  except*: // 错误！
  
  3:  except* 捕获的普通异常会当作异常组处理：
  4:except 和 except*不能混用  这个想法被官方拒绝了，认为这种语法没有增加有用语义，反而提高了复杂性。
  """
# **********************************************************************************
# 通过add_note函数添加字符串到异常的注释中，会出现在回溯中的异常字符串之后
e = ZeroDivisionError("division by zero")

e.add_note("增加注释")
print(e.__notes__)  # 异常的注释列表,这个属性在第一次调用 add_note被创建
print(e)
# raise e  # 异常未被捕获，会抛出异常，显示添加的__notes__,若被正常捕获，不会显示__notes__


try:
    1 / 0
except ZeroDivisionError as e:
    e.add_note("1111111")
    print(e)
    raise e  # 异常被捕获后，可以再次抛出捕获的异常
