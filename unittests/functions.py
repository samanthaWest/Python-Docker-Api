import unittest
from functions.functions import contains_number

class TestFunctions(unittest.TestCase):

    def test_contains_number(self):
        self.assertTrue(contains_number('sam7tha'))
        self.assertFalse(contains_number('samantha'))

if __name__ == '__main__':
    unittest.main()