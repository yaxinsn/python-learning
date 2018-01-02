#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：面向对象高级编程
__slots__来控制向对象进行动态增加属性。
@property: get_attr set_attr的语法糖。
多重继承

'''
print(comment)

###############################################

class Dog(object):
    __slots__ = ('name','age','__color');
    
Dog.color="Red"  ##为类的所有实例配置默认属性。默认属性都是公有的吧？

flopy=Dog();

flopy.name="flopy"
flopy.age=3;
#flopy.__color="yellow" 这句执行出错
#flopy.color="yellow" __slots__之外的属性，执行会出错。

#print("flopy is a %(__color) %(age) old dog!" % flopy); flopy不是一个映射。
print("flopy is a %s %d old dog!" % (flopy.name ,flopy.age) );
