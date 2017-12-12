#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：函数的定义
可变参数：
'''
print(comment)

###############################################





print(u'''可变参数 calc([1,2,3,4,....])''');


def calc(*n):
    sum = 0;
    for i in n:
        sum = sum +i
    return sum



print(calc(1,2,3));
print(calc(1,2,3,3,2,1));

l=[1,1,1,1]
print(calc(*l)); # 这*l是个语法。
