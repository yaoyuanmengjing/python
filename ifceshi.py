# 根据用户输入内容打印其权限

# alex --> 超级管理员
# eric --> 普通管理员
# tony --> 业务主管
# 其他 --> 普通用户
#!/usr/bin/python
#encoding:utf-8
name = raw_input("请输入用户名:")

if name == "alex":
    print "欢迎管理员"
elif  name == "eric":
    print "普通管理员"
elif  name == "tony":
    print "业务主管"
else:
    print "普通用户"
    

