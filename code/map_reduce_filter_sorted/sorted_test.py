#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：高阶函数sorted
我理解的高阶函数就是可以传入函数指针的函数。

题目：
我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

请用sorted()对上述列表分别按名字排序：


'''
print(comment)

###############################################


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_name(n):
    return str.lower(n[0]);


new_list=sorted(L,key=sort_name);
print(new_list);


def sort_count(n):
    return n[1];

nl=sorted(L,key=sort_count,reverse=True);
print(u''' 以成绩由大到小的排名 ''');
print(nl);
