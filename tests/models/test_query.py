import unittest

from python_advanced_search.models.query import Query
from python_advanced_search.models.commands.conditions import OR, NOT, AND
from python_advanced_search.models.commands.expressions import E


class QueryTestCase(unittest.TestCase):
    def test_query_expression(self):
        query = Query().search(expression='expression')

        self.assertEqual(query.str, 'expression')

    def test_query(self):
        query = Query().search(
            indexed='mywebsite.com',
            in_title=E('seo'),
        ).exclude(
            indexed='excluded-website.com'
        )

        self.assertEqual(
            query.str,
            'site:mywebsite.com intitle:"seo" -site:excluded-website.com'
        )

    def test_query_conditions(self):
        query = Query().search(
            indexed=AND('first-and.com', 'second-and.io'),
            in_title=OR('title_1', 'title_2', 'title_3'),
            filetype=NOT('pdf', 'png')
        )

        self.assertEqual(
            query.str,
            'site:(first-and.com AND second-and.io) intitle:(title_1 OR title_2 OR title_3) filetype:(pdf NOT png)'
        )
