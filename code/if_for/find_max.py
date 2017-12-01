#--coding:utf-8--
###############################################
comment = u'''
描述：for语句找出最大的数据。
'''
print(comment)

###############################################

l=[1,5,7,9,4,34,5,6,87,6,5]
def max(t):
    _max=l[0];
    for i in t:
        if i > _max:
            _max = i;
    return _max

print(max(l));



def max1(t):
    _m_id=0;
    for i,v in enumerate(t):
        if v > t[_m_id]:
            _m_id = i;
    return _m_id;


print(" list[%d]=%d is max!" % (max1(l),l[max1(l)]));
