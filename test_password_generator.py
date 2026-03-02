import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        password = generate_password(10, False, False)
        self.assertEqual(len(password), 10)

    def test_include_numbers(self):
        password = generate_password(20, True, False)
        self.assertTrue(any(char.isdigit() for char in password))

    def test_include_symbols(self):
        password = generate_password(20, False, True)
        self.assertTrue(any(not char.isalnum() for char in password))

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_password(0, False, False)

if __name__ == '__main__':
    unittest.main()