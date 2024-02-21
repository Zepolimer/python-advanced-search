import unittest

from python_advanced_search.models.commands.operators import (
    Operator,
    AndOperator,
    NotOperator,
    OrOperator,
    IndexedOperator,
    InTitleOperator,
    FiletypeOperator
)


class OperatorsTestCase(unittest.TestCase):
    def test_operators(self):
        operator = Operator('name')
        self.assertEqual(str(operator), 'name')

        and_operator = AndOperator()
        self.assertEqual(str(and_operator), 'AND')

        not_operator = NotOperator()
        self.assertEqual(str(not_operator), 'NOT')

        or_operator = OrOperator()
        self.assertEqual(str(or_operator), 'OR')

        indexed_operator = IndexedOperator()
        self.assertEqual(str(indexed_operator), 'site:')

        in_title_operator = InTitleOperator()
        self.assertEqual(str(in_title_operator), 'intitle:')

        filetype_operator = FiletypeOperator()
        self.assertEqual(str(filetype_operator), 'filetype:')
