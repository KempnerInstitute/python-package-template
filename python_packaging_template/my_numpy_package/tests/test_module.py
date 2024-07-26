import unittest
import numpy as np
from my_numpy_package.module import add_arrays, multiply_arrays

class TestModule(unittest.TestCase):

    def setUp(self):
        self.array1 = np.array([1, 2, 3])
        self.array2 = np.array([4, 5, 6])

    def test_add_arrays(self):
        result = add_arrays(self.array1, self.array2)
        expected = np.array([5, 7, 9])
        self.assertTrue(np.array_equal(result, expected), f"Expected {expected}, but got {result}")

    def test_multiply_arrays(self):
        result = multiply_arrays(self.array1, self.array2)
        expected = np.array([4, 10, 18])
        self.assertTrue(np.array_equal(result, expected), f"Expected {expected}, but got {result}")

if __name__ == '__main__':
    unittest.main()

