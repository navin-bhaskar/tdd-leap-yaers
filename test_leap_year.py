import unittest

from leap_year_checker import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test__all_years_divisible_by_400__is_leap_year_returns_true(self):
        """All years divisible by 400 ARE leap years (so, for example, 2000 was indeed a leap year)"""
        self.assertEqual(is_leap_year(2000), True)

    def test__all_years_divisible_by_100_but_not_by_400__is_leap_years_returns_false(self):
        """All years divisible by 100 but not by 400 are NOT leap years 
        (so, for example, 1700, 1800, and 1900 were NOT leap years, NOR will 2100 be a leap year),"""
        self.assertEqual(is_leap_year(1700), False)
        self.assertEqual(is_leap_year(1800), False)
        self.assertEqual(is_leap_year(1900), False)

