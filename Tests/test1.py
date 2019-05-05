import unittest
# import h_w as h_w


def my_sum(a, b):
    return a + b


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEquals(my_sum(5, 6), 12)


