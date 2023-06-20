import unittest
import sympy as sp
import numpy as np
from scipy import linalg

# A class called ArrValue with three attributes - value, value_inverse, and value_transpose - 
# that are Numpy arrays representing a 2x2 matrix and its inverse and transpose. 
# An attribute called value_idempotent which is a 2x2 Numpy array representing an idempotent matrix.
class ArrValue:
    value = np.array([[2, 1],
                      [2, 2]])
    value_inverse = np.linalg.inv(value)
    value_transpose = np.transpose(value)
    value_idempotent = np.array([[1, 0], [0, 0]])


# A function to calculate the determinant of a Numpy array using SymPy library.
# If the size of the array is less than its dimension, return 0.
def numpy_determinant(arr):
    if len(sp.Matrix(arr).rref()[1]) < max(np.shape(arr)):
        return 0
    else:
        return np.linalg.det(arr)


# A function to calculate the determinant of a Numpy array using SciPy library.
def scipy_determinant(arr):
    return linalg.det(arr)


# The test class that "imports" from the unittest.TestCase class.
class TestMethods(unittest.TestCase):

    # First test to check if the determinant computed using NumPy and SciPy is the same.
    def test_positive(self):
        arr1 = ArrValue()
        arr_det_np = numpy_determinant(arr1.value)
        arr2 = ArrValue()
        arr_det_sc = scipy_determinant(arr2.value)
        message = "The two determinant values are not equal"
        self.assertEqual(arr_det_np, arr_det_sc, message)

    # Second test to check if the dimension of the array increases by one after adding a new column.
    def test_new_column(self):
        arr1 = ArrValue.value
        original_array = arr1.shape
        arr2 = np.hstack((arr1, np.array([[0],[0]])))
        self.assertEqual(original_array[1] + 1, arr2.shape[1])

    # Third test to check if the inverse of the matrix has been calculated correctly.
    def test_inverse_matrix(self):
        arr1 = ArrValue()
        arr_inv = np.linalg.inv(arr1.value)
        product = arr1.value @ arr_inv
        message = "The matrix has not been inverted correctly"
        self.assertTrue(np.allclose(product, np.eye(arr1.value.shape[0])), message)

    # Fourth test to check if the transpose of the matrix has been calculated correctly.
    def test_transpose_matrix(self):
        arr1 = ArrValue()
        arr_transpose = np.transpose(arr1.value)
        message = "The matrix has not been transposed correctly"
        self.assertTrue(np.allclose(arr_transpose, arr1.value_transpose), message)

    # Fifth test to check if the matrix is idempotent.
    def test_idempotent_matrix(self):
        arr1 = ArrValue()
        arr_idempotent = arr1.value_idempotent
        product = arr_idempotent @ arr_idempotent
        message = "The matrix is not idempotent"
        self.assertTrue(np.allclose(product, arr_idempotent), message)



if __name__ == '__main__':
    print("Fenix Kanat")
    unittest.main()
