


a=[['name',"abl"],['country','China'],['age',2],['grade',2],['level',2]]

print("a change to dict")
da=dict(a)
print(da)


print("test items")

print(da.items())
print("test keys")

print(da.keys())
print("test values")

print(da.values())

#pop, get popitem, formkeys,update, iteritems, iterkeys,
da.pop('age')
print(da);
print(da.get("age","not exist"))
#da.popitem()
