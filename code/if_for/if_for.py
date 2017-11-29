
#--coding:utf-8--
###############################################
comment = u'''
描述：学习if语句 ，for语言
'''
print(comment)

###############################################

a=["1","2",'3']
t=[]
for i in a:
    t.append(int(i))


print("t list is ");
print(t);

num=raw_input("please input you age:");
age = int(num);
if age > 18 :
    print("you are adult!");
elif age < 3 :
    print("you are litte bady")
else:
    print("you are child!");

print("end");




