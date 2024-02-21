import unittest

from python_advanced_search.bing.query import BingQuery


class BingQueryTestCase(unittest.TestCase):
    def test_bing_query(self):
        query = BingQuery().search(
            indexed='bing.fr',
            location='en',
        )

        self.assertEqual(
            query.str,
            'site:bing.fr location:en'
        )

    def test_bing_query_with_exclude(self):
        query = BingQuery().search(
            indexed='bing.fr',
            in_text='microsoft',
        ).exclude(
            link_domain='teams'
        )

        self.assertEqual(
            query.str,
            'site:bing.fr inbody:microsoft -linkdomain:teams'
        )
