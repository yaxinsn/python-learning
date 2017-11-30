
# -*- coding: utf-8 -*-
#--coding:utf-8--
###############################################
comment = u'''
描述: for与闭包的学习
my_range(n) 函数与range(n)一样。
使用yield 把函数变成一个生成器。
'''
print(comment)

###############################################

def my_range(n):
    t =0;
    while t < n:
        a=t;
        t+=1;
        yield a 

fa=my_range(3);
print(fa);
print(next(fa))
print(next(fa))

print(list(my_range(3)));
