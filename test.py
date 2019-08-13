import unittest
from main import *

class tests(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sum(1,2), 3)
        self.assertEqual(sum(-66,-2), -68)
 
if __name__ == '__main__':
    unittest.main()