#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：函数的定义
位置参数；
默认参数；
命名参数：
可变参数：
'''
print(comment)

###############################################



print(u'''位置参数：add(x,y) ''');

def add(x,y):
    return x+y;


print(add(2,3));


print(u'''默认参数：add(y,x=9,z=3) x=9是默认参数，默认参数必须放在位置参数的后面 ''');

def add(y,x=9,z=3):
    return x+y+z;


print(add(3));



print(u'''可变参数 calc([1,2,3,4,....])''');


def calc(*n):
    sum = 0;
    for i in n:
        sum = sum +i
    return sum



print(calc(1,2,3));
print(calc(1,2,3,3,2,1));



print(u''' 关键字参数 def func(**kw) ''');

def person(name,age,**kw):
    print("name is :",name,'age is ',age,"other:",kw);


person("coco",3,city="beijing",number=1234);


print('-------------------------------------------');

print(u'''命名参数 是指在调用时，为每一个参数加个形参名： ''');

def my_person(name,city,number):
    print("%s is in %s, his Number is %s" % (name,city,number))


def my_bjing_person(name,number,city="BeiJing"):
    my_person(name,city,number);



print(u''' 命令参数的调用方式  my_person(city="Tianjin",name="lala",number="123"); 其中  city ,names的位置与位置形参不一致。但解释器通过命名的指定就了解了参数的意义。''');
my_person(city="Tianjin",name="lala",number="123");

print(u''' my_bjing_person("lili","3456")''');

my_bjing_person("lili","3456");
