#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：try except
'''
print(comment)

###############################################


'''
"捕获所有的异常"
try:
    x=input("Enter the first Number:")
    y=input("Enter the second Number:")
    print x/y;
except:
    print "some thing is wrong!"
'''

"捕获异常的对象，并打印出来"
try:
    x=input("Enter the first Number:")
    y=input("Enter the second Number:")
    print x/y;
except (ZeroDivisionError, TypeError), e:
    print "x/0 is heppened, os bad!"
    print e;


