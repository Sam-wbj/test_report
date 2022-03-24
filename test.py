# *encoding=utf-8
import itertools


# 第一题
def merge_dict(x, y):
    if x == y:
        raise ValueError('需要两个不同参数！')
    z = {}
    if not hasattr(x, 'keys') or not hasattr(y, 'keys'):
        return y if isinstance(y, str) else y.values()
    keys = set(x) & set(y)
    for key in keys:
        z[key] = merge_dict(x[key], y[key])
    for key in set(x) - keys:
        z[key] = x[key]
    for key in set(y) - keys:
        z[key] = y[key]
    return z


# 第二题
def func(string):
    tel_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    num_list = []
    res_ist = []
    for num in string:
        num_list.append(tel_map[num])
    for i in itertools.product(*num_list):
        res_ist.append(''.join(i))
    return res_ist


# 第三题
'''
内存泄漏是指，当python创建对象时申请了一块内存空间，使用完后没有释放，由于没有释放，这块内存区域其他类加载的时候无法申请，
同时当前类又没有这块内存空间的内存地址了也无法使用，相当于丢了一块内存，这就是内存泄漏。 
'''
# 循环引用导致内存泄露
a = []
b = []
a.append(b)
b.append(a)
del a
del b

'''
1、创建对象a后，内存的引用计数器为1；
2、创建对象b后，内存的引用计数器为1；
3、当执行a.append(b)时，对象b内存的引用计数器为2；
4、当执行b.append(a)时，对象a内存的引用计数器为2；
5、当执行del a后，内存的引用计数器为1；
6、当执行del b后，内存的引用计数器为1；
7、虽然a、b对象可以被销毁，但是他们的引用计数器都为1，导致垃圾回收器不会回收它们，所以会内存泄露。

'''

# if __name__ == '__main__':
    # source_dict = {'key0': [1, 23, 4], 'key1': [32, 4], 'key2': {'inner_key0': 3, 'inner_key1': 'd'}}
    # update_dict = {'key1': 'x', 'key2': {'inner_key0': 'y'}}
    #
    # # res = merge_dict(source_dict, update_dict)
    # res = func('23')
    #
    # print res
