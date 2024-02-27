import unittest

from python_advanced_search.engines.bing.commands.operators import (
    IndexedUrlOperator,
    InTextOperator,
    LocationOperator,
    LanguageOperator,
    LinkFromDomainOperator,
    LinkDomainOperator,
)


class OperatorsTestCase(unittest.TestCase):
    def test_operators(self):
        operator = IndexedUrlOperator()
        self.assertEqual(str(operator), 'url:')

        operator = InTextOperator()
        self.assertEqual(str(operator), 'inbody:')

        operator = LocationOperator()
        self.assertEqual(str(operator), 'location:')

        operator = LanguageOperator()
        self.assertEqual(str(operator), 'language:')

        operator = LinkFromDomainOperator()
        self.assertEqual(str(operator), 'linkfromdomain:')

        operator = LinkDomainOperator()
        self.assertEqual(str(operator), 'linkdomain:')
