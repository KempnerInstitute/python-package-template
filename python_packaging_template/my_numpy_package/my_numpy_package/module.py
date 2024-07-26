import numpy as np

def add_arrays(array1, array2):
    """
    Adds two NumPy arrays element-wise.

    Parameters:
    array1 (numpy.ndarray): First array.
    array2 (numpy.ndarray): Second array.

    Returns:
    numpy.ndarray: Element-wise sum of array1 and array2.
    """
    return np.add(array1, array2)

def multiply_arrays(array1, array2):
    """
    Multiplies two NumPy arrays element-wise.

    Parameters:
    array1 (numpy.ndarray): First array.
    array2 (numpy.ndarray): Second array.

    Returns:
    numpy.ndarray: Element-wise product of array1 and array2.
    """
    return np.multiply(array1, array2)
