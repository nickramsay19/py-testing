# py-testing - A simple showcase of testing in python with unittest
> Created by Nicholas Ramsay

## main.py
```python
def sum(a,b):
    return a + b
```

## test.py
```python
import unittest
from main import *

class tests(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sum(1,2), 3)
        self.assertEqual(sum(-66,-2), -68)
 
if __name__ == '__main__':
    unittest.main()
```