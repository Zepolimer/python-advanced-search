import unittest

from python_advanced_search.google.commands.operators import (
    AllInTitleOperator,
    InTextOperator,
    AllInTextOperator,
    InUrlOperator,
    AllInUrlOperator,
    InAnchorOperator,
    AllInAnchorOperator,
    RelatedOperator,
    DefineOperator
)


class OperatorsTestCase(unittest.TestCase):
    def test_operators(self):
        operator = AllInTitleOperator()
        self.assertEqual(str(operator), 'allintitle:')

        operator = InTextOperator()
        self.assertEqual(str(operator), 'intext:')

        operator = AllInTextOperator()
        self.assertEqual(str(operator), 'allintext:')

        operator = InUrlOperator()
        self.assertEqual(str(operator), 'inurl:')

        operator = AllInUrlOperator()
        self.assertEqual(str(operator), 'allinurl:')

        operator = InAnchorOperator()
        self.assertEqual(str(operator), 'inanchor:')

        operator = AllInAnchorOperator()
        self.assertEqual(str(operator), 'allinanchor:')

        operator = RelatedOperator()
        self.assertEqual(str(operator), 'related:')

        operator = DefineOperator()
        self.assertEqual(str(operator), 'define:')
