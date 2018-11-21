from time import ctime, sleep
import multiprocessing


def talk(content, loop):
    for i in range(loop):
        print("Talks: %s %r" % (content, ctime()))
        sleep(2)


def write(content, loop):
    for j in range(loop):
        print("Write: %s %r" % (content, ctime()))
        sleep(4)

process = []

t1 = multiprocessing.Process(target=talk, args=('Talks1', 3))
process.append(t1)

t2 = multiprocessing.Process(target=write, args=('Write1', 3))
process.append(t2)

if __name__ == '__main__':
    for p in process:
        p.start()
    for p in process:
        p.join()
    print("Final: Final: %r" % ctime())
