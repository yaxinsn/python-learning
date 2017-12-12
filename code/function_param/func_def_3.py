#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：函数的定义
关键字参数
'''
print(comment)

###############################################




print(u''' 关键字参数 def func(**kw) kw是dict展开。 ''');

def person(name,age,**kw):
    print("name is :",name,'age is ',age,"other:",kw);
    print("City",kw.get("city"));

person("coco",3,city="beijing",number=1234);

vivi={'name':"ViVi", 'city':"dalian",'number':1234}; # name 不能再定义了。
vivi={ 'city':"dalian",'number':1234}; 
person("vivi",4,**vivi);



print('-------------------------------------------');

