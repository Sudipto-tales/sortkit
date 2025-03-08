import unittest
from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort, heap_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        """Define test cases"""
        self.test_cases = [
            ([5, 3, 8, 6, 2, 7, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
            ([100, 50, 25, 75, 10], [10, 25, 50, 75, 100]),
            ([3], [3]),
            ([], [])
        ]

    def test_bubble_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(bubble_sort(arr[:]), expected)

    def test_selection_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(selection_sort(arr[:]), expected)

    def test_insertion_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(insertion_sort(arr[:]), expected)

    def test_quick_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(quick_sort(arr[:]), expected)

    def test_merge_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(merge_sort(arr[:]), expected)

    def test_heap_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(heap_sort(arr[:]), expected)

if __name__ == "__main__":
    unittest.main()
