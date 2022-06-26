import unittest
from stack import *



class TestStack(unittest.TestCase):

    def setUp(self):
        self.s = Stack()
        self.assertEqual(self.s.size(), 0)
        self.s.push(1)
        self.s.push('Hello')
        self.s.push(4.6)
        self.s.push(True)

    def tearDown(self):
        self.s = None

    def test_size(self):
        self.assertEqual(self.s.size(), 4)

    def test_push(self):
        self.assertEqual(self.s.push(5), None)
        self.assertEqual(self.s.push(10), None)
        self.assertEqual(self.s.push(20), None)
        with self.assertRaises(NullElementException):
            self.s.push(None)
            raise NullElementException("Value should not be Null")
        with self.assertRaises(NullElementException):
            self.s.push('')
            raise NullElementException("Value should not be Null")

    def test_pop(self):
        self.assertNotEqual(self.s.pop(),  False)
        self.assertEqual(self.s.pop(),  4.6)
        self.assertEqual(self.s.pop(),  'Hello')
        self.assertEqual(self.s.pop(),  1)
        with self.assertRaises(EmptyStackException):
            self.s.pop()
            raise EmptyStackException("Stack is empty")

    def test_peak(self):
        self.assertEqual(self.s.peak(),  True)
        self.assertNotEqual(self.s.peak(),  4.6)
        self.s.pop()
        self.assertEqual(self.s.peak(),  4.6)
        self.s.pop()
        self.assertEqual(self.s.peak(),  'Hello')
        self.s.pop()
        self.assertEqual(self.s.peak(),  1)
        self.s.pop()

        with self.assertRaises(EmptyStackException):
            self.s.peak()
            raise EmptyStackException("Stack is empty")

    def test_isEmpty(self):

        self.assertFalse(self.s.isEmpty(), False)
        self.s.pop()
        self.assertFalse(self.s.isEmpty(), False)
        self.s.pop()
        self.assertFalse(self.s.isEmpty(), False)
        self.s.pop()
        self.assertFalse(self.s.isEmpty(), False)
        self.s.pop()
        self.assertTrue(self.s.isEmpty(), True)

if __name__ == '__main__':
    unittest.main()
