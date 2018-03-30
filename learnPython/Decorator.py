# 装饰器 Decorator
# 在函数调用前后自动完成一些操作，但又不希望修改当前函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# decorator就是一个返回函数的高阶函数
# 定义一个获取当前时间的函数
# def  getTime():
# 	import time
# 	print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

# T = getTime
# T()		# 2018-03-19

# 通过__name__属性可以拿到函数名
# print(T.__name__)		# getTime

# 定义装饰器
def log(fn):
	def wrapper(*args, **kw):
		print('call %s():' % fn.__name__)
		return fn(*args, **kw)
	return wrapper

@log
def  getTime():
	import time
	print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

getTime()
# 把@log放到getTime()函数的定义处，相当于执行了语句：getTime = log(getTime)
print(getTime.__name__)		# wrapper
# 此时getTime函数的__name__属性已经变为wrapper，因为经过装饰器的修饰，最终调用的是wrapper函数，所以wrapper的name也就赋值给了getTime
# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
def log(fn):
	import functools
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		print('call %s():' % fn.__name__)
		return fn(*args, **kw)
	return wrapper

