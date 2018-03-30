# 偏函数（Partial function）把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 比如int函数的默认值是10（十进制），那么假如此时的需求是大量数据需要转化为二级制，每次调用int函数都要输入base参数并显示的设置其默认值为2，
# 偏函数则可以快速的生成一个int2函数，此函数的默认值即为2（二进制）
import functools
int2 = functools.partial(int, base=2)
print(int2('10'))