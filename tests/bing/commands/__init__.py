import unittest

from python_advanced_search.models.commands import Expression
from python_advanced_search.bing.commands import (
    IndexedUrlCommand,
    InTextCommand,
    LocationCommand,
    LanguageCommand,
    LinkFromDomainCommand,
    LinkDomainCommand,
)


class CommandsTestCase(unittest.TestCase):
    def test_commands(self):
        expression = Expression('expression_value')

        # IndexedUrlCommand
        command = IndexedUrlCommand(expression=expression)

        self.assertEqual(
            command.str,
            'url:expression_value'
        )

        # InTextCommand
        command = InTextCommand(expression=expression)

        self.assertEqual(
            command.str,
            'inbody:expression_value'
        )

        # LocationCommand
        command = LocationCommand(expression=expression)

        self.assertEqual(
            command.str,
            'location:expression_value'
        )

        # LanguageCommand
        command = LanguageCommand(expression=expression)

        self.assertEqual(
            command.str,
            'language:expression_value'
        )

        # LinkFromDomainCommand
        command = LinkFromDomainCommand(expression=expression)

        self.assertEqual(
            command.str,
            'linkfromdomain:expression_value'
        )

        # LinkDomainCommand
        command = LinkDomainCommand(expression=expression)

        self.assertEqual(
            command.str,
            'linkdomain:expression_value'
        )
