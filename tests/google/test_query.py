import unittest

from python_advanced_search.google.query import GoogleQuery


class GoogleQueryTestCase(unittest.TestCase):
    def test_google_query(self):
        query = GoogleQuery().search(
            indexed='google.fr',
            all_in_title='search',
        )

        self.assertEqual(
            query.str,
            'site:google.fr allintitle:search'
        )

    def test_google_query_with_exclude(self):
        query = GoogleQuery().search(
            indexed='google.fr',
            all_in_anchor='anchor',
        ).exclude(
            in_anchor='scholar'
        )

        self.assertEqual(
            query.str,
            'site:google.fr allinanchor:anchor -inanchor:scholar'
        )
