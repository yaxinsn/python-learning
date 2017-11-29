
# -*- coding: utf-8 -*-

#####################################################

comment='''请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']

#--coding:utf-8--
'''
print(comment);
#########################################################


L = ['Bart', 'Lisa', 'Adam']

for i in L :
    print("hello %s!" % i)



t=0
while t <len(L):
    print(" Hello %s" % L[t])
    t+=1;

print("exit!");

