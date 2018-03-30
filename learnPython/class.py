# python 面向对像编程
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student (object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))
bart = Student('Carlos', 100)
# print(bart)			# <__main__.Student object at 0x0000000001E900B8>
# print(Student)		# <class '__main__.Student'>
# bart是一个实例，Student是一个class，实例的__main__指向类，类的__main__为自身，object at 0x0000000001E900B8为存在内存的地址
# bart.print_score()


# Python的私有变量
# Python私有变量__name以双下划线开头命名的变量即为私有变量

# Python 继承在声明类时传入需要继承的父类即可

# 使用__slots__
# Python允许声明类或者初始化实例后动态的给类或者实例绑定属性和方法，但是此时就存在怎样限制这些动态添加的属性和方法的问题，
# 比如在类上添加了一个say的方法，那么所有实例都会共享这个方法，__slots__就是为了限制这个方法的
class Students (object):
	__slots__ = ('name', 'age')		# 利用tuple定义哪些属性允许被绑定

s = Students()
s.name = 'Carlos'
s.age = 18
s.score = 100		# 报错'Students' object has no attribute 'score'
