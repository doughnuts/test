"""

生成器函数，生成的是一个生成器对象们必须使用next()去调用yield去拿到值,生成器函数的执行过程是在next()的时候执行的
"""


def gen():
    print(100)
    yield 10
    yield 11
    yield 12
    print(100)



g=gen()
print(g)
# print(next(g))
# print(next(g))




"""

递归函数
步骤：
1.定义函数
2.结束条件
    n=1
3.找规律
    n！=n*(n-1)!
4.调用函数本身

递：分解
归：合并
"""
def factorial(n):
    if n==0 or n==1:
        return 1

    return n*factorial(n-1)

res=factorial(5)
print(res)




"""
斐波拉契数列

"""


def get_rabbit_num(month):
    if month<0:
        return NotImplemented
    if month==1 or month==2:
        return 1
    return get_rabbit_num(month-1)+get_rabbit_num(month-2)

res=get_rabbit_num(20)
print(res)