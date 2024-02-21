import unittest

from python_advanced_search.models.commands.expressions import Expression
from python_advanced_search.models.commands.operators import Operator
from python_advanced_search.models.commands import (
    Command,
    ExpressionCommand,
    ExactExpressionCommand,
    IndexedCommand,
    InTitleCommand,
    FiletypeCommand,
)


class CommandsTestCase(unittest.TestCase):
    def test_commands(self):
        expression = Expression('expression_value')
        operator = Operator('operator_name:')

        # Command
        command = Command(
            expression=expression,
            operator=operator
        )

        self.assertEqual(
            command.str,
            'operator_name:expression_value'
        )

        # Command without operator param
        command_without_operator = Command(
            expression=expression
        )

        self.assertEqual(
            command_without_operator.str,
            'expression_value'
        )

        # ExpressionCommand
        expression_command = ExpressionCommand(
            expression=expression
        )

        self.assertEqual(
            expression_command.str,
            'expression_value'
        )

        # ExactExpressionCommand
        exact_command = ExactExpressionCommand(
            expression='exact_expression_value'
        )

        self.assertEqual(
            exact_command.str,
            '"exact_expression_value"'
        )

        # IndexedCommand
        indexed_command = IndexedCommand(
            expression=expression
        )

        self.assertEqual(
            indexed_command.str,
            'site:expression_value'
        )

        # InTitleCommand
        in_title_command = InTitleCommand(
            expression=expression
        )

        self.assertEqual(
            in_title_command.str,
            'intitle:expression_value'
        )

        # FiletypeCommand
        filetype_command = FiletypeCommand(
            expression=expression
        )

        self.assertEqual(
            filetype_command.str,
            'filetype:expression_value'
        )
