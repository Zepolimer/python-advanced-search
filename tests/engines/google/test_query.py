import unittest

from python_advanced_search.engines.google.query import GoogleQuery


class GoogleQueryTestCase(unittest.TestCase):
    def test_google_query(self):
        query = GoogleQuery().include(
            indexed='google.fr',
            all_in_title='search',
        )

        self.assertEqual(
            query.str,
            'site:google.fr allintitle:search'
        )
        self.assertEqual(
            query.encoded_str,
            'q=site%3Agoogle.fr+allintitle%3Asearch'
        )

    def test_google_query_with_exclude(self):
        query = GoogleQuery().include(
            indexed='google.fr',
            all_in_anchor='anchor',
        ).exclude(
            in_anchor='scholar'
        )

        self.assertEqual(
            query.str,
            'site:google.fr allinanchor:anchor -inanchor:scholar'
        )
        self.assertEqual(
            query.encoded_str,
            'q=site%3Agoogle.fr+allinanchor%3Aanchor+-inanchor%3Ascholar'
        )
