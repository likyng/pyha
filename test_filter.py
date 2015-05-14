# deduplication Hausaufgabe
# https://github.com/likyng/pyha/blob/master/test_filter.py

from filter import deduplicate
import unittest

class TestDeduplicate(unittest.TestCase):
    def test_deduplicate_numbers(self):
        dedup = deduplicate([1, 1, 2])
        result = [1, 2]
        self.assertEqual(result, dedup)

    def test_deduplicate_noargs(self):
        dedup = deduplicate([])
        result = []
        self.assertEqual(result, dedup)

    def test_deduplicate_text(self):
        dedup = deduplicate(['h', 'h', 'g', 2, 2])
        result = ['h', 'g', 2]
        self.assertEqual(result, dedup)

    def test_deduplicate_trice(self):
        dedup = deduplicate(['h', 'h', 'h', 'g', 2, 2])
        result = ['h', 'g', 2]
        self.assertEqual(result, dedup)

    def test_deduplicate_neg(self):
        dedup = deduplicate(['h', 'h', 'h', 'g', -2, -2])
        result = ['h', 'g', -2]
        self.assertEqual(result, dedup)
