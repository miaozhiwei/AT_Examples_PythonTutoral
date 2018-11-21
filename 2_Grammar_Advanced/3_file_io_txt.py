f = open('d:\\123.txt', 'r')

# 每次读一行，指针下移。
# print(f.readline())
# print(f.readline())
# print(f.readline())

# 读取文件所有内容。
# print(f.read())

# 读取文件所有内容（list形式）。
# print(f.readlines())

lines = f.readlines()
print(lines)
for line in lines:
    print(line.split(',')[1])

f.close()
