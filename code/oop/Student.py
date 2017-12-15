#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：面向对象oops
关键字：class object __init__(self,*args,**kw)
__XX__前后都有下划线是：特殊变量，可以直接访问
__XXXX               :是私有变量，不可以直接访问。
'''
print(comment)

###############################################


class Student(object):
    def __init__(self,name,score):
        self.__name=name;
        self.__score=score;
    def show_score(self):
        print("%s score=%d"% (self.__name,self.__score));

lisa=Student("lisa",88);
mona=Student("mona",82);


#print("lisa's score:",lisa.__score); 此时不能再访问__score

print("show_score:");
lisa.show_score();
