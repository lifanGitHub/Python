names = ['Michael_', 'Bob_', 'Tracy_']
for name in names:
    print(name, end="")

print("---------------------------------")

# python内置id()函数，这个函数用于返回对象的唯一标识（identity）。对象实际内存地址为hex(id(obj))，本文我将id()和内存地址划等号。
# 内置函数is()，用于比较两个对象的identity是否一样，举例：
classmates = ['Michael', 'Bob', 'Tracy']
a = ['Michael', 'Bob', 'Tracy']
b = ['Michael', 'Bob', 'Tracy']
print(hex(id(classmates)))
print(a == b)
print(a is b)

print("---------------------------------")

print(ord("a"))
print(chr(97))
print(str("\u4e2d\u6587"))

print(10/3)
print(10//3)



