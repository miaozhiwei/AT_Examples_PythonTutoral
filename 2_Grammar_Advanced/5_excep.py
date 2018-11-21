# try:
#     filename = input("Enter the name of file:")
#     open("d:\\\%s" % filename)
# except FileNotFoundError:
#     print("File[%s] not found." % filename)

# try:
#     print(stu)
# except NameError:
#     print("Name1 is not defined.")

# try:
#     print(stu)
# except BaseException:
#     print("Name2 is not defined.")

# try:
#     #stu = "joseph"
#     print(stu)
# except BaseException as msg:
#     print("Error:", msg)
# else:
#     print("Good Luck! stu is defined.")
# finally:
#     print("the end.")


def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Zero not allowed.")
    return x/y

try:
    a = div(5, 0)
    print(a)
except BaseException as msg:
    print(msg)
