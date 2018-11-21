from time import ctime, sleep
import threading


def talk(content, loop):
    for i in range(loop):
        print("Talks: %s %r" % (content, ctime()))
        sleep(2)


def write(content, loop):
    for j in range(loop):
        print("Write: %s %r" % (content, ctime()))
        sleep(4)

threads = []

t1 = threading.Thread(target=talk, args=('Talks1', 3))
threads.append(t1)

t2 = threading.Thread(target=write, args=('Write1', 3))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Final: Final: %r" % ctime())
