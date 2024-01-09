import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import PIL as pil


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def curve():
    xdata = np.linspace(0, 4, 50)
    y = func(xdata, 2.5, 1.3, 0.5)
    rng = np.random.default_rng()
    y_noise = 0.2 * rng.normal(size=xdata.size)
    ydata = y + y_noise
    plt.plot(xdata, ydata, 'b-', label='data')

    popt, pcov = sp.optimize.curve_fit(func, xdata, ydata)
    plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')
    plt.show()


# open and resize a jpeg image
def jpegReduce():
    img = pil.Image.open("C:/Users/coren/OneDrive/Images/doge.jpg")
    img2 = img.resize((200, 200))
    img.show()
    img2.show()
