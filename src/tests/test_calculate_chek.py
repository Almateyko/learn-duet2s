import unittest
from src.main_program import *


class TestMainProgram(unittest.TestCase):

    def test_calculate_chek_1(self):
        a = dict(gas=0, water=0, electricity=0)
        self.assertEqual('Verification was successful', calculate_chek('gas', 3, a))
        self.assertEqual('Verification was successful', calculate_chek('water', 12, a))
        self.assertEqual('Verification was successful', calculate_chek('electricity', 124, a))
        self.assertEqual('Verification was successful', calculate_chek('gas', 10, a))
        self.assertEqual('Verification was successful', calculate_chek('water', 88, a))

    def test_calculate_chek_2(self):
        a = dict(gas=0, water=0, electricity=0)
        self.assertEqual('ValueError', calculate_chek('gas', -2, a))
        self.assertEqual('ValueError', calculate_chek('water', -20, a))
        self.assertEqual('ValueError', calculate_chek('gas', 1342, a))
        self.assertEqual('ValueError', calculate_chek('gas', 1042354, a))
        self.assertEqual('ValueError', calculate_chek('water', 'a', a))
        self.assertEqual('ValueError', calculate_chek('water', 'qwerty', a))

    def test_calculate_chek_3(self):
        a = dict(gas=0, water=0, electricity=0)
        self.assertEqual('TypeError', calculate_chek('gas', [1, 2, 3], a))
        self.assertEqual('TypeError', calculate_chek('water', {'one': 12, 15: 'adds'}, a))

    def test_calculate_chek_4(self):
        a = dict(gas=0, water=0, electricity=0)
        self.assertEqual('Verification was unsuccessful', calculate_chek('gas', '', a))


if __name__ == '__main__':
    unittest.main()
