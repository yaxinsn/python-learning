#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：面向对象高级编程
为实例动态增加方法和属性，
为类动态增加方法和属性。
__slots__来控制向对象进行动态增加属性。
@property: get_attr set_attr的语法糖。
多重继承

'''
print(comment)

###############################################


class Student(object):
    def __init__(self,name,score):
        self.__name=name;
        self.__score=score;
        self.__grade=3;
        self.grade=3;

    def show_grade(self):
        print("%s __grade=%d"% (self.__name,self.__grade));
        print("%s grade=%d"% (self.__name,self.grade));
        
    def show_score(self):
        print("%s score=%d"% (self.__name,self.__score));

lisa=Student("lisa",88);
mona=Student("mona",82);


#print("lisa's score:",lisa.__score); 此时不能再访问__score

print("show_score:");
lisa.show_score();

print("""######################MethodType为一个实例增加方法##########################""")
def set_age(self,age):
    self.age=age;

from types import MethodType

lisa.set_age = MethodType(set_age,lisa);

lisa.set_age(4);

print("lisa age %d"% lisa.age);
print("""######################为一个类动态增加方法##########################""")

def set_grade(self,grade):
    self.__grade = grade; ##实测发现，此函数调用后__grade 还是原值。__grade是私有变量。只能被class里的“静态方法”来修改。
    self.grade = grade;   ##此函数调用后，grade的值被修改了。grade是公开变量。可以被动态方法来修改。
#    print("%s grade is %d"% (self.__name, self.grade));

Student.setGrade = set_grade;

new_mona=Student("mona",2);
new_mona.show_grade();

new_mona.setGrade(30);


new_mona.show_grade();

print(""" lisa的定义在Student.setGrade之前，但是lisa也可以使用setGrade这个方法。 """);
lisa.setGrade(4);
lisa.show_grade();
