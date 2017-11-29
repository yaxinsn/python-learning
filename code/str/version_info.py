#--coding:utf-8--
###############################################
comment = u'''
功能描述：得到python的版本信息。
##############################################
'''
print(comment)

###############################################
'''
'''
def sys_ver():
    import sys
    print("sys version:");
    print(sys.version)
    print(sys.version_info)
    print(sys.version_info.major)

def sys_ver_maj():
    import sys
    return sys.version_info.major


def plat_ver():
        import platform
        print("platform version:");
        print(platform.python_version())


plat_ver()
sys_ver();

if sys_ver_maj() == 2:
    print("the python is V2");
elif sys_ver_maj() == 3:
    print("the python is V3");
