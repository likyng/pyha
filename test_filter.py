# deduplication Hausaufgabe
# https://github.com/likyng/pyha/blob/master/test_filter.py

from filter import deduplicate
import unittest

class TestDeduplicate(unittest.TestCase):
    def test_deduplicate(self):
        dedup = deduplicate([1, 1, 2])
        result = [1, 2]
        self.assertEqual(result, dedup)
