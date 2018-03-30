# 测试
name = '王小二'
money = 100
blance = 20
# print('亲爱的%s,您的话费为%d,余额为%d' % (name, 100, 20));
def testFn (n):
	for num in range(0,n):
		print(num)
		if num >= 1:
			print(num*100)
		else: 
			print(num)

# 定义函数求解一元二次方程
import math
def quadratic (a, b ,c):
	x = b * b - 4 * a * c
	if x >= 0:
		y = math.sqrt(x)
		return ((-b + y) / 2 * a), ((-b - y) / 2 * a)
	else:
		return '对不起，无解'
# print(quadratic(1,2,3));

# 函数的可变参数
def  cacl (numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

# 传入数组或者元组
# print(cacl([1,2,3]))
# print(cacl((1,2,3)))

def cacl1 (*numbers):	# *代表可变参数
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
# print(cacl1(1,2,3))

# 当可变参数需要传入一个数组或者元组时可以将实参作为可变参数加*传入
num = [1,2,3]
# print(cacl1(*num));

# 关键字参数 类似缺醒参数，可以传入任意多个关键字参数，多个关键字参数会组成字典
def person (name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

# 关键字参数可以不传
# person('Carlos', 18)

# 多个关键字参数
# person('Carlos', 18, city='BeiJing', hobby='girl')

# 传入字典作为关键字参数
extra = {'city': 'BeiJing', 'hobby': 'girl', 'jop': 'Enginner'}
# person('Carlos', 18, **extra);

# 命名关键字参数
def person (name, age, *, city, job):	# 仅允许传入city和job关键字的参数，其他会报错
	print(name, age, city, job)

# person('Carlos', 18, city='Beijing', job= 'Enginner')
# person('Carlos', 18, city='Beijing', hobby='girl')		# 报错

#当函数中已经定义了一个可变参数，再定义关键字参数时则不需要中间的*作为分隔了
def  person (name, age, *args, city, job):
	sum = 0
	print(args)
	if args:
		for n in args:
			print(type(n));
			sum = sum + n
	print(name, age, sum, city, job)

# person('Carlos', 18, city='Beijing', job= 'Enginner')
# person('Carlos', 18, 1, 2, 3, city='Beijing', job= 'Enginner')	# 可变参数会自动在函数中组成元组

# python中可以组合各种参数使用，但是使用顺序必须为：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def product (*args):
	sum = 1
	if (type(args) == type([])) or (type(args) == type(())):
		for n in args:
			sum = sum * n
	elif type(args) == int:
		sum = sum * n
	return sum
# print(product(0))
# print(product(1,2,3,4))

# 递归函数
def recursion (n):
	if n == 1:
		return 1
	return n * (n - 1)
# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
	# print(key)

# 迭代key
# for value in d.values():
	# print(value)

# 迭代key和value
# for k, v in d.items():
	# print(k, v)
# 判断当前对像是否可迭代
# from collections import Iterable
# isinstance('abc', Iterable)

# 利用enumerate方法模拟java的for循环
# for i, value in enumerate(['A', 'B', 'C']):
	# print(i, value)

# 可以利用多个参数解构循环内部数据
# for x, y in [(1, 1), (2, 2), (3, 3)]:
	# print(x, y)
# 迭代查找一个list中最小和最大值，并返回一个tuple
l = [1, 2, 3, 0, 5, 10]

def findMinMax (l):
	l = l if l else []
	if l == []:
		return (None, None)
	else:
		max = l[0]
		min = l[0]
		for k in l:
			if max < k:
				max = k
			if min > k:
				min = k
		return (min, max)
# print(findMinMax(l))

# 列表生成
L = []
for x in range(1, 11):
	L.append(x * x)
# print(L)
# 列表生成式
L = [x * x for x in range(1, 11)]
# print(L)
L = [x * x for x in range(1, 11) if x % 2 == 0]
# print(L)
L = [x * y for x in range(1, 11) for y in range(20, 30)]
# print(L)
# 列出当前目录所有文件
import os
# print([d for d in os.listdir('.')])
# 
# 生成器：生成器通过一定的规则生成列表
# 列表生成
L = [x * x for x in range(10)]
# 生成器生成
g = (x *x for x in range(10))
print(g)	# <generator object <genexpr> at 0x0000000001DF4938> 
 # 生成器元素获取
# print(next(g))		# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
# 使用next()方法不方便，生成器是可迭代的对像，利用for循环可以获得指定元素
# 斐波那契数列
def  fib (max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'over'

# fib(8)
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def  fib (max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'over'

# print(fib(8))    <generator object fib at 0x0000000002164A40>
# for x in fib(8):
# 	print(x)		
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def  fn ():
	print('step1')
	yield 1
	print('step2')
	yield 2
	print('step3')
	yield 3
# f = fn()
# print(next(f))		# 先打印step1 在打印1 可以推断出执行过程为先按照函数执行顺序从上往下执行，遇到print执行打印step1，然后执行yield，结束第一次next
# next(f)				# 第二次执行从上次执行位置开始继续执行
# next(f)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
# f = fib(8)
# while True:
# 	try:
# 		print('f:', next(f))
# 	except StopIteration as e:				# 当触发迭代器stop时跳出循环
# 		print('return valus:', e.value)
# 		break
# 利用生成器（generator）输出杨辉三角
def rectangle(n):
	m, b = 0, [1]
	while m < n:
		yield b
		b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
		m += 1

# for x in rectangle(10):
# 	print(x)




