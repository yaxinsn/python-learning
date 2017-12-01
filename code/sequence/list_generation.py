#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：列表生成式
List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
[x * x for x in range(1, 11) if x % 2 == 0]
 [m + n for m in 'ABC' for n in 'XYZ']
[s.lower() for s in L]

练习

如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
 L = ['Hello', 'World', 18, 'Apple', None]

 isinstance(s,str) 用于判断是不是str，返回 True,False.

'''
print(comment)

###############################################
L = ['Hello', 'World', 18, 'Apple', None]
l=[s.lower() for s in L if isinstance(s,str)]
print("result: " );
print(l);

