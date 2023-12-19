import matplotlib.pyplot as plt
import random as rd
import numpy as np
from matplotlib import cm

def nombres_aleatoire(taille):
    nb_list = []
    for i in range(taille):
        nb_list.append(rd.random()*10)
    return nb_list
def courbes():
    plt.subplot(2, 2, 1)
    plt.plot(nombres_aleatoire(100), 'r--')
    plt.xlabel('Trucs')
    plt.ylabel('Machin')
    plt.legend(['Bonjour'])
    plt.subplot(2, 2, 2)
    plt.plot(nombres_aleatoire(100), 'g-^')
    plt.xlabel('Bidule')
    plt.ylabel('Chouette')
    plt.legend(['Hello'])
    plt.subplot(2, 2, 3)
    plt.plot(nombres_aleatoire(100), 'b*')
    plt.legend(['Hola'])
    plt.xlabel('Feur')
    plt.ylabel('Quoi')
    plt.subplot(2, 2, 4)
    plt.plot(nombres_aleatoire(100), 'y+')
    plt.legend(['Guten Tag'])
    plt.xlabel('Hello world')
    plt.ylabel('Lorem Ipsum')
    plt.annotate('Ceci est une flèche', xy=(50, 7), xytext=(65, 5.5), arrowprops={'facecolor':'black', 'shrink':0.5} )
    plt.show()
def histo():
    plt.hist(nombres_aleatoire(100), bins=10, color='r', orientation='horizontal')
    plt.show()
def pie():
    plt.pie(nombres_aleatoire(5))
    plt.show()

def la3d():
    plt.style.use('_mpl-gallery')

    # Make data
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.cos(R) * Y *X

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    plt.show()
la3d()