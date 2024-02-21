import unittest

from python_advanced_search.models.commands import Expression
from python_advanced_search.google.commands import (
    AllInTitleCommand,
    InTextCommand,
    AllInTextCommand,
    InUrlCommand,
    AllInUrlCommand,
    InAnchorCommand,
    AllInAnchorCommand,
    RelatedCommand,
    DefineCommand
)


class CommandsTestCase(unittest.TestCase):
    def test_commands(self):
        expression = Expression('expression_value')

        # AllInTitleCommand
        command = AllInTitleCommand(expression=expression)

        self.assertEqual(
            command.str,
            'allintitle:expression_value'
        )

        # InTextCommand
        command = InTextCommand(expression=expression)

        self.assertEqual(
            command.str,
            'intext:expression_value'
        )

        # AllInTextCommand
        command = AllInTextCommand(expression=expression)

        self.assertEqual(
            command.str,
            'allintext:expression_value'
        )

        # InUrlCommand
        command = InUrlCommand(expression=expression)

        self.assertEqual(
            command.str,
            'inurl:expression_value'
        )

        # AllInUrlCommand
        command = AllInUrlCommand(expression=expression)

        self.assertEqual(
            command.str,
            'allinurl:expression_value'
        )

        # InAnchorCommand
        command = InAnchorCommand(expression=expression)

        self.assertEqual(
            command.str,
            'inanchor:expression_value'
        )

        # AllInAnchorCommand
        command = AllInAnchorCommand(expression=expression)

        self.assertEqual(
            command.str,
            'allinanchor:expression_value'
        )

        # RelatedCommand
        command = RelatedCommand(expression=expression)

        self.assertEqual(
            command.str,
            'related:expression_value'
        )

        # DefineCommand
        command = DefineCommand(expression=expression)

        self.assertEqual(
            command.str,
            'define:expression_value'
        )
