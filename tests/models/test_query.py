import unittest

from python_advanced_search.models.query import Query
from python_advanced_search.models.commands.conditions import OR, NOT, AND
from python_advanced_search.models.commands.expressions import E


class QueryTestCase(unittest.TestCase):
    def test_query_expression(self):
        query = Query()
        query.include(expression='expression')

        self.assertEqual(query.str, 'expression')
        self.assertEqual(
            query.encoded_str,
            'q=expression'
        )

    def test_query(self):
        query = Query()
        query.include(
            indexed='mywebsite.com',
            in_title=E('seo'),
        ).exclude(
            indexed='excluded-website.com'
        )

        self.assertEqual(
            query.str,
            'site:mywebsite.com intitle:"seo" -site:excluded-website.com'
        )
        self.assertEqual(
            query.encoded_str,
            'q=site%3Amywebsite.com+intitle%3A%22seo%22+-site%3Aexcluded-website.com'
        )

    def test_query_conditions(self):
        query = Query()
        query.include(
            indexed=AND('first-and.com', 'second-and.io'),
            in_title=OR('title_1', 'title_2', 'title_3'),
            filetype=NOT('pdf', 'png')
        )

        self.assertEqual(
            query.str,
            'site:(first-and.com AND second-and.io) intitle:(title_1 OR title_2 OR title_3) filetype:(pdf NOT png)'
        )
        self.assertEqual(
            query.encoded_str,
            'q=site%3A%28first-and.com+AND+second-and.io%29+intitle%3A%28title_1+OR+title_2+OR+title_3%29+filetype%3A%28pdf+NOT+png%29'
        )
