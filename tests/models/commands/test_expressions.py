import unittest

from python_advanced_search.models.commands.expressions import Expression, E


class ExpressionsTestCase(unittest.TestCase):
    def test_expression(self):
        expression = Expression('expression')

        self.assertEqual(
            expression.value,
            'expression'
        )

        exclude_expression = Expression(
            value='exclude_expression',
            exclude=True
        )

        self.assertEqual(
            exclude_expression.value,
            '-exclude_expression'
        )

    def test_exact_expression(self):
        exact_expression = E('exact_expression')

        self.assertEqual(
            exact_expression.value,
            '"exact_expression"'
        )

        exclude_exact_expression = E(
            value='exclude_exact_expression',
            exclude=True
        )

        self.assertEqual(
            exclude_exact_expression.value,
            '-"exclude_exact_expression"'
        )
