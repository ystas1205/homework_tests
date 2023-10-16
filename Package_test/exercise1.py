from Package_main.main2 import putting_things_in_order
from Package_main.main import all_names, unique_names
from Package_main.main3 import vote
import unittest
from parameterized import parameterized


class Test_main(unittest.TestCase):

    def test_putting_things_in_order(self):
        # тест на сортировку по длительности курса
        list_duration = [int(data[-2:]) for data in putting_things_in_order()]
        self.assertEqual(sorted(list_duration), list_duration)

    def test_unique_names(self):
        # проверка на уникальность имен
        list_unique_names = [i for i in unique_names().split(',')]
        expected = [data.split()[0] for data in all_names()]
        self.assertEqual(len(list_unique_names), len(set(expected)))


class Test_main3(unittest.TestCase):
    # тест на наиболее частый элемент в списке
    @parameterized.expand([
        ([2, 3, 5, 5, 5, 1], 5),
        ([0, 0, 0, 1, 2], 0),
        ([3, 1, 2, 2, 2], 2),
        ([2, 5, 3, 3, 3], 3),
    ])
    def test_vote(self, a, expected):
        result = vote(a)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
