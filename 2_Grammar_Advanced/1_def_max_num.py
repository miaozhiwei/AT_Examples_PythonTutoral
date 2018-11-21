# 定义功能函数/方法

def max_num(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return x

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = max_num(a, b)
print(c)
