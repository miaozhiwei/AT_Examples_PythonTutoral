# 元组用的小括号，不能修改，其他和列表一样
# 列表和元组可以相互转化

print('----------------------------------')

l = ['Joseph', 'Kate', 'Tony', 'Luke']
print(l)#下标0开始
print(l[2], l[-1])

print('----------------------------------')

#add
l.append('Cherry')
print(l)
l.insert(3, 'Nope')
print(l)
print(l[1:5])#左包含，右不包含

print('----------------------------------')

#modify
l[1] = 'Puk'
print(l)

print('----------------------------------')
print(l)

#delete
l.pop()#删除最后一位
print(l)

l.pop(-1)#删除最后一位
print(l)

l.pop(2)
print(l)

print(len(l))

print('----------------------------------')

tlp = tuple(l)#列表转化到元组
print(tlp)

lst = list(tlp)#元组转化到列表
print(lst)
