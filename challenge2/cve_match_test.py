import unittest
from cve_match import cve_match


class TestCveExtract(unittest.TestCase):
    valid_cve = 'CVE-2019-9740'

    def test_single_example(self):
        expected = 'CVE-2019-9740'
        self.assertCountEqual([expected], cve_match(expected))

    def test_multiple_example(self):
        self.assertCountEqual([self.valid_cve, 'CVE-2020-9740'],
                              cve_match(self.valid_cve + " hello " + 'CVE-2020-9740'))

    def test_repeats_are_returned(self):
        self.assertCountEqual([self.valid_cve] * 3, cve_match(' '.join([self.valid_cve] * 3)))

    def test_must_have_at_least_4_digits(self):
        self.assertCountEqual([], cve_match('CVE-2019-974'))

    def test_cve_must_be_upper_case(self):
        self.assertCountEqual([], cve_match('cve-2019-9740'))

    def test_must_have_dash_as_separator(self):
        self.assertCountEqual([], cve_match('CVE_2019_9740'))

    def test_must_have_4_digit_year(self):
        self.assertCountEqual([], cve_match('CVE-199-9740'))

    def test_years_before_1999_ignored(self):
        self.assertCountEqual([], cve_match('CVE-1998-9740'))

    def test_years_1999_accepted(self):
        expected = 'CVE-1999-9740'
        self.assertCountEqual([expected], cve_match(expected))

    def test_years_after_2999_ignored(self):
        self.assertCountEqual([], cve_match('CVE-3000-9740'))

    def test_years_2999_accepted(self):
        expected = 'CVE-2999-9740'
        self.assertCountEqual([expected], cve_match(expected))

    def test_0_as_years_ignored(self):
        self.assertCountEqual([], cve_match('CVE-0000-9740'))

    def test_cve_required(self):
        self.assertCountEqual([], cve_match('CE-0000-9740'))

    def test_more_than_7_digits_number_ignored(self):
        self.assertCountEqual([], cve_match('CE-0000-97400000'))

    def test_7_digit_trailing_number_accepted(self):
        self.assertCountEqual([], cve_match('CE-0000-9740000'))
