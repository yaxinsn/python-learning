
#--coding:utf-8--
###############################################
comment = u'''IP地址转成32进制数
python3以后print是一个函数，不再是一个语句。

python3 的string.atoi is null
在for语句的语句块中，不能使用int(i) i是字符串列表的迭代ID。
不适用于python3
'''
print(comment)

###############################################
import string as tr

ip="10.11.12.13"

ip_str_list=ip.split('.');
print(ip_str_list) 

t=[]
for i in ip_str_list:
    t.append(tr.atoi(i))


print("t list is ");
print(t);




ip_int=0
t=0
for i in ip_str_list :
    ip_int +=(tr.atoi(i))<<(8*(3-t))
    t=t+1;
print(u"输出结果：")
print(ip_int)
print("ip_int 0x%08x" % ip_int)
