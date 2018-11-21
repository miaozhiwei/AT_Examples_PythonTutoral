import csv

csv_f = csv.reader(open('d:\\123.csv', 'r'))

# 逐行读取
for line in csv_f:
    print(line)

stu1 = ['Mary', 28, 'Changsha']
stu2 = ['Carrie', 22, 'Nanjing']

# w 代表写，a代表追加
csv_w = csv.writer(open('d:\\123.csv', 'a',newline=''), dialect='excel')

csv_w.writerow(stu1)
csv_w.writerow(stu2)

print('done')
