# 一个线程按顺序执行
from time import ctime, sleep


def talk():
    print("test1: %r" % ctime())
    sleep(2)


def speak():
    print("test2: %r" % ctime())
    sleep(3)


if __name__ == '__main__':
    talk()
    speak()
    print("test3: %r " % ctime())
