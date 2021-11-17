# import unittest


# class TestSum(unittest.TestCase):

#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# if __name__ == '__main__':
#     unittest.main()

import unittest
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)
        a=6
        b=8
        # self.assertIs(a,b)

class TestSub(unittest.TestCase):
    def test_sub_5(self):
        self.assertEqual(12-5,7)

if __name__ == '__main__':
    unittest.main()