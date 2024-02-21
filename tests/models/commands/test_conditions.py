import unittest

from python_advanced_search.models.commands.conditions import OR, AND, NOT


class ConditionsTestCase(unittest.TestCase):
    def test_or_condition(self):
        condition = OR('keyword_1', 'keyword_2')

        self.assertEqual(
            condition.expression.value,
            'keyword_1 OR keyword_2'
        )

    def test_and_condition(self):
        condition = AND('keyword_3', 'keyword_4')

        self.assertEqual(
            condition.expression.value,
            'keyword_3 AND keyword_4'
        )

    def test_not_condition(self):
        condition = NOT('keyword_5', 'keyword_6')

        self.assertEqual(
            condition.expression.value,
            'keyword_5 NOT keyword_6'
        )
