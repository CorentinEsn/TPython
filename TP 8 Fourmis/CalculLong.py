import threading as th
import psutil as psu
import multiprocessing as mp


def calcul_long():
    n = 1E7
    while n > 0:
        n -= 1
    print(" All good")


def print_cpu_usage():
    # Utilisation du CPU par coeur
    cpu_percent_per_core = psu.cpu_percent(percpu=True)
    for i, core_percent in enumerate(cpu_percent_per_core):
        print(f"Core {i + 1} Usage: {core_percent}%")

    # Charge moyenne du systeme au cours des 1, 5 et 15 dernieres minutes
    load_average = psu.getloadavg()
    print(f"Load Average (1min, 5min, 15min): {load_average}")

    # Utilisation globale du CPU
    overall_cpu_percent = psu.cpu_percent()
    print(f"Overall CPU Usage: {overall_cpu_percent}%")


def use_processes():
    if __name__ == '__main__':
        # Creation de deux processus
        print ("------------- Processus ----------------")
        print("\n")
        process1 = mp.Process(target=calcul_long)
        process2 = mp.Process(target=calcul_long)
        process3 = mp.Process(target=calcul_long)
        process4 = mp.Process(target=calcul_long)

        # Demarrage des processus
        process1.start()
        process2.start()
        process3.start()
        process4.start()

        # Afficher l'utilisation du CPU pendant que les processus s'executent
        print_cpu_usage()
        print("-----------------------------------")
        print("\n")
        # Attendre que les processus se terminent
        process1.join()
        process2.join()
        process3.join()
        process4.join()


def use_threads():
    print("------------- Threads ----------------")
    print("\n")
    # Creation de deux threads
    thread1 = th.Thread(target=calcul_long)
    thread2 = th.Thread(target=calcul_long)
    thread3 = th.Thread(target=calcul_long)
    thread4 = th.Thread(target=calcul_long)

    # Demarrage des threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Afficher l'utilisation du CPU pendant que les threads s'executent
    print_cpu_usage()
    print("----------------------------------")
    print("\n")
    # Attendre que les threads se terminent
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()


use_threads()
use_processes()
