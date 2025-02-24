import unittest

from leap_year_checker import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test__all_years_divisible_by_400__is_leap_year_returns_true(self):
        """All years divisible by 400 ARE leap years (so, for example, 2000 was indeed a leap year)"""
        self.assertEqual(is_leap_year(2000), True)

