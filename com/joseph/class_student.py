# 用于外部引用的Demo
# 类：用来描述具有相同的属性和方法的对象的集合
# 方法：类中定义的函数

class Student():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        print("I am %s, I am %d years old. I come from %s." % (name, age, city))

# str1 = Student("Joseph1", 25, "BeiJing")
# str2 = Student("Joseph2", 32, "ShangHai")

