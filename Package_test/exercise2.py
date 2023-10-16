import unittest
from Package_main.folder import create_folder


class Test_creating_a_folder(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(create_folder('test'), 201)

    def test_checking_folder(self):
        self.assertEqual(create_folder('test'), 409)


if __name__ == '__main__':
    unittest.main()
