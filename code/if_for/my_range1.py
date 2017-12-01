
# -*- coding: utf-8 -*-
#--coding:utf-8--
###############################################
comment = u'''
描述: for与闭包的学习
my_range(n) 函数与range(n)一样。返回一个迭代器。
'''
print(comment)

###############################################

def my_range(n):
    t =0;
    def __range():
        while t < n:
            a=t;
            t+=1;#这一行出错。python的闭包不能修改upvalue变量吗？
            return a
        return None;
    return __range;

fa=my_range(3);
print(fa);
print((fa()))
print((fa()))

print(list(my_range(3)));
