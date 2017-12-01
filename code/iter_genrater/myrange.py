#--coding:utf-8--
##print 
# str = reqr = `` 
###############################################
comment = u'''
描述：myrange函数，返回一个list.
	myxrange函数，返回一个生成器，生成器就是可迭代的。
  迭代器由类来完成
   必须有__iter__()和next()方法

这两个方法是迭代器最基本的方法，一个用来获得迭代器对象，一个用来获取容器中的下一个元素。

class object self __init__几个关键字完成的一个迭代器类，
还有一个高级迭代器，可以传入参数的。

'''
print(comment)

###############################################

def myrange(n):
    l=[];
    t=0
    while t<n:
        l.append(t);
        t+=1;
    return l;

print("myrange 4")
print(myrange(4));


############################### 有yield,p这是生成器。
def myxrange(n):
    t=0;
    while t<n:
        yield t;
        t+=1;

print("myxrange 4");
x=myxrange(4);
print(x);
print(type(x));
print(x.next())


class myrange_1(object):
    def __init__(self,n):
        self.id=0;
        self.max=n;

    def __iter__(self):
        return self
   
    def next(self):
        if self.id < self.max:
            v=self.id;
            self.id+=1;
            return v;
        else:
            raise StopIteration();

m=myrange_1(4); # 4-给了__init__里的n.
print(u''' m是一个iterotor ''');
print('type m is %s ' % type(m));
print('print m:  %s ' % type(m));
for i in m:
    print(i)
print(u''' 高级迭代器 ''')


class myrange_2(object):
    def __init__(self,n,f):
        self.id=0;
        self.max=n;
	self.f=f

    def __iter__(self):
        return self
   
    def next(self):
        if self.id < self.max:
            v=self.f(self.id);
            self.id+=1;
            return v;
        else:
            raise StopIteration();
def power(n): 
    return n*n
m=myrange_2(4, power); # 4-给了__init__里的n.
print(u''' m是一个iterotor ''');
print('type m is %s ' % type(m));
print('print m:  %s ' % type(m));
for i in m:
    print(i)
