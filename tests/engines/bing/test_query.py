import unittest

from python_advanced_search.engines.bing.query import BingQuery


class BingQueryTestCase(unittest.TestCase):
    def test_bing_query(self):
        query = BingQuery().include(
            indexed='bing.fr',
            location='en',
        )

        self.assertEqual(
            query.str,
            'site:bing.fr location:en'
        )
        self.assertEqual(
            query.encoded_str,
            'q=site%3Abing.fr+location%3Aen'
        )

    def test_bing_query_with_exclude(self):
        query = BingQuery().include(
            indexed='bing.fr',
            in_body='microsoft',
        ).exclude(
            link_domain='teams'
        )

        self.assertEqual(
            query.str,
            'site:bing.fr inbody:microsoft -linkdomain:teams'
        )
        self.assertEqual(
            query.encoded_str,
            'q=site%3Abing.fr+inbody%3Amicrosoft+-linkdomain%3Ateams'
        )
