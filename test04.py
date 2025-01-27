d1 = {"a":100,"b":55,"c":79,"d":33}

#按照key排序
#items得到的是kv，没有给出key函数，默认按照key排序


list01=sorted(d1.items(), key=lambda x:x[1])
print(list01)




list02=sorted(d1.items(), key=lambda x:x[0])
print(list02)

a=10
b=20

f = lambda x,y:x if x>y else y

print(f(a,b))


#关键字参数解包
def jiebao(**kwargs):
    print(kwargs)
    print(kwargs["a"])
    for k,v in kwargs.items():
        print(k,v)


jiebao(a=1,b=2,c=3)



#内置函数
'''
abs() 绝对值
ascii() 
bin()  二进制数
bool()
chr()  chr(97)返回字符串"a"
dict() 
divmod()  返回商和余数
enumerate 返回可迭代对象的索引和值，元组形式
eval()  执行字符串表达式
help():内置的帮助函数
hex()  十六进制
ord():返回字符的ASCII码
round():四舍六入五取偶
zip():木桶原理，将两个可迭代对象的元素一一对应，按照少的元素进行对应
'''

print(divmod(7, 3))
print(round(3.5))
print(round(4.5))


#冒泡排序

list03=[1,3,5,7,9,2,4,6,8,0]
for i in range(len(list03)-1):
    for j in range(len(list03)-1-i):
        if list03[j]>list03[j+1]:
            list03[j],list03[j+1]=list03[j+1],list03[j]
print(list03)


#类型注解
def out(a:int,b:int)->int:

    return a+b
print(out(1, 2))




#模式匹配

nums=[10,11]

match nums:
    case list():
        print("list")

    case tuple():
        print("tuple")


















