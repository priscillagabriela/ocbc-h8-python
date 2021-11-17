from fractions import Fraction
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

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

# class TestSub(unittest.TestCase):
#     def test_sub_5(self):
#         self.assertEqual(12-5,7)