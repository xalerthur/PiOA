import unittest
import subprocess
import io
import sys
import os
import numpy as np
sys.path.append(sys.path[0] + '/..')
from PiOA_3a import strassen

class TestPiOA_3a(unittest.TestCase):

    def test_matrix(self):
        # define random matrix
        matA = np.random.randint(10, size=(4, 4))
        matB = np.random.randint(10, size=(4, 4))

        res = strassen(matA, matB)
        expected = matA * matB
        print(matA)
        print(matB)
        print(res)
        print(expected)
        # self.assertEqual(strassen(matA, matB), matA * matB)
        self.assertTrue(np.array_equal(res, expected))   

    def test1(self):
        matA = np.array(
            [[2, 4, 7, 3],
            [3, 8, 1, 6],
            [5, 1, 1, 5],
            [4, 1, 6, 7]]
        )                  
        matB = np.array(
            [[1, 2, 3, 4],
            [8, 7, 6, 5],
            [9, 0, 1, 2],
            [9, 9, 4, 3]]
        )

        res = strassen(matA, matB)
        expected = matA * matB
        self.assertTrue(np.array_equal(res, expected))  

    def test2(self):
        matA = np.array(
            [[3, 4, 2, 0],
            [1, 4, 4, 3],
            [0, 5, 6, 1],
            [5, 9, 4, 3]]
        )                  
        matB = np.array(
            [[0, 6, 4, 3]
            [0, 9, 1, 0]
            [5, 2, 1, 9]
            [7, 0, 4, 3]]
        )

        res = strassen(matA, matB)
        expected = matA * matB
        self.assertTrue(np.array_equal(res, expected))  

        
if __name__ == '__main__':
    print(sys.path)
    # sys.path.insert(1, os.getcwd())

    unittest.main()