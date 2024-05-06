import unittest
from Task_3 import factorial
import time

class TestCase(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        print(self.start_time)

    def test_factorial(self):
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(True),1)
        self.assertRaises(ValueError,factorial,-5)
        self.assertRaises(ValueError,factorial,9223372036854775807)  #sys.maxsize
        self.assertRaises(TypeError,factorial,"a")
        self.assertRaises(TypeError,factorial,[3])
    def tearDown(self):
        self.ourTime=self.start_time-time.time()
        print(self.ourTime)  #Если честно, то я не знаю, почему оно не выводиться
