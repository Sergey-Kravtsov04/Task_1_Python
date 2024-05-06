import unittest
from Task_3 import factorial
import time

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.start_time = time.time()

    def test_factorial(self):
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(True),1)
        self.assertRaises(ValueError,factorial,-5)
        self.assertRaises(ValueError,factorial,9223372036854775807)  #sys.maxsize
        self.assertRaises(TypeError,factorial,"a")
        self.assertRaises(TypeError,factorial,[3])
    def tearDown(self) -> None:
        t=self.start_time-time.time()
        print(t)
