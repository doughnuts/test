# letters="abcndafifaifidfhjidifi"
#
# results={}
# #
# # for letter in letters:
# #     if letter in results:
# #         results[letter] += 1
# #     else:
# #         results[letter] = 1
# #
# # for k,v in results.items():
# #     a="{}:{}".format(k,v)
# #     print(a)
#
# print("--------------------")
#
#
#
# #update功能传入一个字典，如果字典中有key则更新value，没有则添加。 get方法获取字典中的value,获取到就+1，没有获取到就将value值设置为defualt=0
# for letter in letters:
#     results.update({letter:results.get(letter,0) + 1})
# print(results)











def add(a,b):
    return a+b

a=float(input())
b=float(input())
print(add(a, b))






