# 高阶函数---map()reduce()filter()
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	return x * x

r = map(f, [1,2,3,4,5,6])		# 返回一个生成器赋值到r
# print(list(r))				# 利用列表生成列表

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def  add (x, y):
	return x + y
# print(reduce(add, [1,2,3,4,5]))

# 将列表的首字母大写
def  fn (s):
	return s.capitalize()

a = map(fn, ['adam', 'LISA', 'barT'])
# print(list(a))

# 利用reduce求解list的乘积
def prod (x, y):
	return x * y

b = reduce(prod, [3, 5, 7, 9])
# print(b)

# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 利用filter过滤偶数
def is_odd(num):
	return num % 2 == 1
l = list(filter(is_odd, [1,2,3,4,5,6,7,8,9]))
# print(l)

# sorted()排序
# 可以接收一个key函数来实现自定义的排序
l = sorted([1, 2, 21, -15, 30, -2], key = abs, reverse = True)
# print(l)
# reverse参数接收布尔值，代表是否反向list




