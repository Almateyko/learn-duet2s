import unittest
from src.dict_functions import dict_write_chek


class TestDictFunction(unittest.TestCase):

    def test_dict_write_chek_1(self):
        self.assertEqual('Verification was successful', dict_write_chek('constants', 1))
        self.assertEqual('Verification was successful', dict_write_chek('constants', 12))
        self.assertEqual('Verification was successful', dict_write_chek('constants', 124))
        self.assertEqual('Verification was successful', dict_write_chek('constants', 10))
        self.assertEqual('Verification was successful', dict_write_chek('constants', 88))

    def test_dict_write_chek_2(self):
        self.assertEqual('ValueError', dict_write_chek('constants', -2))
        self.assertEqual('ValueError', dict_write_chek('constants', -20))
        self.assertEqual('ValueError', dict_write_chek('constants', 1342))
        self.assertEqual('ValueError', dict_write_chek('constants', 1042354))
        self.assertEqual('ValueError', dict_write_chek('constants', 'a'))
        self.assertEqual('ValueError', dict_write_chek('constants', 'qwerty'))

    def test_dict_write_chek_3(self):
        self.assertEqual('TypeError', dict_write_chek('constants', [1, 2, 3]))
        self.assertEqual('TypeError', dict_write_chek('constants', {'one': 12, 15: 'adsc'}))
        self.assertEqual('TypeError', dict_write_chek({'free': 12, 15: 'awful'}, 1))
        self.assertEqual('TypeError', dict_write_chek([1, 2, 3], 2))

    def test_dict_write_chek_4(self):
        self.assertEqual('Verification was unsuccessful', dict_write_chek('constants', ''))


if __name__ == '__main__':
    unittest.main()
