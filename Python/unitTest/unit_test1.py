import unittest

def add(a,b):
    return a+b 

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3,5),8,"add(3,5) returned some number other than 8")
    def test_add_negative_numbers(self):
        self.assertEqual(add(-3,-5),-8,"add(-3,-5) returned some number other than -8")
    def test_add_mix_numbers(self):
        self.assertEqual(add(3,-5),-2,"add(3,-5) returned some number other than -2")
    

if __name__ == '__main__':
    unittest.main()