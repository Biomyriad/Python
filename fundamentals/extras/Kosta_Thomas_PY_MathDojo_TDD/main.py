import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

class Md_test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(Md_test.md.add(1,2).result,3)
        self.assertEqual(Md_test.md.add(4,5,6).result,18)
        self.assertEqual(Md_test.md.add(6,7,8,9).result,48)

    def testTwo(self):
        self.assertEqual(Md_test.md.subtract(1,2).result, 45)
        self.assertEqual(Md_test.md.subtract(4,5,6).result, 30)
        self.assertEqual(Md_test.md.subtract(6,7,8,9).result, 0)

    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")

    @classmethod
    def setUpClass(cls):
        cls.md = MathDojo()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()