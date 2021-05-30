import unittest
from src.main_program import *


class TestMainProgram(unittest.TestCase):

    def test_calculate_chek_1(self):
        self.assertEqual('Verification was successful', calculate_chek('gas', 3))
        self.assertEqual('Verification was successful', calculate_chek('water', 12))
        self.assertEqual('Verification was successful', calculate_chek('electricity', 124))
        self.assertEqual('Verification was successful', calculate_chek('any', 10))
        self.assertEqual('Verification was successful', calculate_chek('way', 88))

    def test_calculate_chek_2(self):
        self.assertEqual('ValueError', calculate_chek('gas', -2))
        self.assertEqual('ValueError', calculate_chek('water', -20))
        self.assertEqual('ValueError', calculate_chek('gas', 1342))
        self.assertEqual('ValueError', calculate_chek('gas', 1042354))
        self.assertEqual('ValueError', calculate_chek('water', 'a'))
        self.assertEqual('ValueError', calculate_chek('water', 'qwerty'))

    def test_calculate_chek_3(self):
        self.assertEqual('TypeError', dict_write_chek('gas', [1, 2, 3]))
        self.assertEqual('TypeError', dict_write_chek('water', {'one': 12, 15: 'adds'}))

    def test_calculate_chek_4(self):
        self.assertEqual('Verification was unsuccessful', dict_write_chek('gas', ''))


if __name__ == '__main__':
    unittest.main()
