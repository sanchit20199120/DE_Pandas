
# Testing name_function.py file function using unittest2 module

import unittest2
from name_function import get_formatted_name


class NameTestCase(unittest2.TestCase):
    """Test's for name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('sanchit','bhardwaj')
        self.assertEqual(formatted_name, 'Sanchit Bhardwaj')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('sanchit','bhardwaj','kumar')
        self.assertEqual(formatted_name, 'Sanchit Kumar Bhardwaj')



if __name__ == '__main__':
    unittest2.main()

# run the file using terminal
