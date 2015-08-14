# -*- coding: utf-8 -*-
"""Tests for the random item selector."""
from fauxfactory import gen_selectpick
import unittest


class TestSelect(unittest.TestCase):
    """Test random select."""
    def test_no_elements_at_all(self):
        self.assertEqual(0, len(gen_selectpick([], 0)))

    def test_no_elements_to_pick(self):
        self.assertEqual(0, len(gen_selectpick(range(100), 0)))

    def test_same_elements(self):
        src = [1, 2, 3]
        res = sorted(gen_selectpick(src, len(src)))
        self.assertEqual(src, res)

    def test_quiet_fail_on_more_elements(self):
        src = [1, 2, 3]
        res = sorted(gen_selectpick(src, len(src) + 1, quiet=True))
        self.assertEqual(src, res)

    def test_correct_pick(self):
        src = range(100)
        n = 10
        res = gen_selectpick(src, n)
        for number in res:
            self.assertIn(number, src)
        self.assertEqual(n, len(res))

    def test_raises_error_if_not_quiet(self):
        src = [1]
        n = 2  # larger than len(src)
        self.assertRaises(ValueError, gen_selectpick, src, n, quiet=False)
