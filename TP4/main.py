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

    n_radii = 8
    n_angles = 36

    # Make radii and angles spaces
    radii = np.linspace(0.125, 1.0, n_radii)
    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)[..., np.newaxis]

    # Convert polar (radii, angles) coords to cartesian (x, y) coords.
    x = np.append(0, (radii * np.cos(angles)).flatten())
    y = np.append(0, (radii * np.sin(angles)).flatten())
    z = np.sin(-x * y)

    # Plot
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.plot_trisurf(x, y, z, vmin=z.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    plt.show()

la3d()