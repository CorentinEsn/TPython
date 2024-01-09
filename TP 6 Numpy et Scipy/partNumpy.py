import numpy as num


# Créer un tableau de dimension 3 avec un shape de (4, 3, 2) rempli avec des nombres aléatoires
# affiche les attributs du tableau : ndim, shape, size, dtype, itemsize, data.
def createArray():
    tab = num.random.random((4, 3, 2))
    print(tab, "\n", "ndim : ", tab.ndim, "\n", "shape : ", tab.shape, "\n", "size : ", tab.size, "\n", "dtype : ",
          tab.dtype, "\n", "itemsize : ", tab.itemsize, "\n", "data : ", tab.data)


def matrixProduct():
    m1 = num.random.randint(0, 8, (3, 3))
    m2 = num.random.randint(2, 10, (3, 3))
    print("m1\n", m1, "\n" * 2, "m2\n", m2, "\n" * 2, "m1*m2\n", m1 * m2, "\n" * 2, "m1.m2\n", m1.dot(m2), "\n" * 2,
          "m1 transpose\n", m1.transpose())


def matrixDetAndInv():
    m1 = num.random.randint(0, 9, (3, 3))
    print("m1\n", m1, "\n" * 2, "det m1 :", num.linalg.det(m1), "\n" * 2, "inv m1\n", num.linalg.inv(m1), "\n" * 2,
          "valeurs propres\n", num.linalg.eigvals(m1), "\n" *2, "vecteurs propres\n", num.linalg.eig(m1)[1])
