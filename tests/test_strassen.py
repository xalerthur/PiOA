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
        # self.assertEqual(strassen(matA, matB), matA * matB)
        self.assertTrue(np.array_equal(res, expected))                            
if __name__ == '__main__':
    print(sys.path)
    # sys.path.insert(1, os.getcwd())

    unittest.main()