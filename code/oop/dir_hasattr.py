
#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：type(134)==int
     dir()函数列出这个变量的类型所拥有的所有方法与属性。
     getattr
     hasattr
     setattr 对一个对象动态地增加（绑定）属性和方法。
     以上三个函数，可以针对属性也可以针对方法。感觉在python里对属性和方法区别不大，只要使用时有区别吧。
     
     为一个对象绑定一个新的属性可以使用setattr(),也可以直接使用puppy.y=0, puppy.func=new_func;

----------------------------------------------------------      
'''
print(comment)

###############################################

class Animal(object):
    def __init__(self,name):
        self.__name__=name;
    def getname(self):
        return self.__name__;


puppy=Animal("puppy")

print(puppy.getname());

t=hasattr(puppy,'__name__');
print("puppy has __name__is ",t);


t=hasattr(puppy,'getname');
print("puppy has getname is ",t);
t=hasattr(puppy,'setname');
print("puppy has setname is ",t);



def setname(self, name):
    self.__name__=name;

setattr(puppy,'setname',setname);

t=hasattr(puppy,'setname');
print("puppy has setname is ",t);

print("call puppy.setname");

puppy.setname(puppy,"PUppy");#这个方法是后加的，需要在使用时，需要传入self。
print("puppy new name %s" % puppy.getname());

print("--------------------------------------");
print("puppy.y=9");
puppy.y=9

puppy.SETNAME=setname;
print(dir(puppy))
