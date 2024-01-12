import threading as th
import multiprocessing as mp
import psutil as ps


def calcul_long(name):
    print(name + " Start")
    n = 1E7
    while n > 0:
        n -= 1
    print(name + " All good")

def usage():
    print("cpu time :", ps.cpu_times())
    print("cpu count :", ps.cpu_count())
    print("cpu precent :", ps.cpu_percent(), "%")
    print("vmem :", ps.virtual_memory())


if __name__ == '__main__':
    t1 = th.Thread(target=calcul_long, args="a")
    t3 = th.Thread(target=calcul_long, args="c")
    t2 = th.Thread(target=calcul_long, args="b")

    p1 = mp.Process(target=calcul_long, args="x")
    p2 = mp.Process(target=calcul_long, args="y")
    p3 = mp.Process(target=calcul_long, args="z")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    usage()

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    usage()

