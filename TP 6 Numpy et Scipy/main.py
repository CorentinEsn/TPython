import partNumpy
import partScipy


def NumFunctions():
    partNumpy.createArray()
    print("~" * 20)
    partNumpy.matrixProduct()
    print("~" * 20)
    partNumpy.matrixDetAndInv()


def ScipyFunctions():
    partScipy.curve()
    partScipy.jpegReduce()


NumFunctions()
print("~" * 20, "\n", "~" * 20)
ScipyFunctions()
