import urllib.parse

from python_crawler.crawler import GoogleRequest, BingRequest

from python_advanced_search.models.commands.expressions import Expression
from python_advanced_search.models.commands import (
    ExpressionCommand,
    ExactExpressionCommand,
    IndexedCommand,
    InTitleCommand,
    FiletypeCommand,
)
from python_advanced_search.engines.bing.commands import (
    IndexedUrlCommand,
    InBodyCommand,
    LocationCommand,
    LanguageCommand,
    LinkFromDomainCommand,
    LinkDomainCommand
)
from python_advanced_search.engines.google.commands import (
    AllInTitleCommand,
    InTextCommand,
    AllInTextCommand,
    InUrlCommand,
    AllInUrlCommand,
    InAnchorCommand,
    AllInAnchorCommand,
    RelatedCommand,
    DefineCommand,
)
from python_advanced_search.models.location import Location


class Query:
    """
    Base class with commons operators

    For inheritance :
        - override **_operators list by implementing search engine's operator names
        - override add_commands() by implementing custom commands
    """

    _operators = [
        'expression',
        'exact_expression',
        'indexed',
        'in_title',
        'filetype'
    ]

    def __init__(self):
        self.commands = []

    @property
    def str(self):
        query = []
        for command in self.commands:
            query.append(command.str)

        query_str = ' '.join(query)
        return query_str

    @property
    def encoded_str(self):
        return urllib.parse.urlencode({'q': self.str})

    @staticmethod
    def __class_factory(class_name, expr, exclude=False):
        """
        <ClassName>Command factory if imported and existing command class
            :param str class_name: <ClassName>Command
            :param str expr: searched expression
            :param bool exclude: False by default
            :return: <ClassName>Command
        """
        cls = globals()[class_name]
        expression = expr

        if isinstance(expression, str):
            expression = Expression(expr)

        return cls(
            expression=expression,
            exclude=exclude
        )

    def _add_commands(self, exclude=False, **_operators):
        """
        Use this method to add command <operator:value>
            :param bool exclude: False by default
            :param **kwargs _operators: kwargs list
        """

        for operator, expr in _operators.items():
            class_name = '%sCommand' % operator.title().replace('_', '')

            try:
                cls = self.__class_factory(class_name, expr, exclude)
                self.commands.append(cls)
            except KeyError:
                raise Exception('--- Class [%s] does not exist ---' % class_name)

    def include(self, **_operators):
        """ Include one OR many <expression> or <operator:expression>

        Optional keyword arguments:
            - expression        --  expression
            - indexed           --  site:domain.tld
            - in_title          --  intitle:expression
            - filetype          --  filetype:ext
        """

        self._add_commands(**_operators)
        return self

    def exclude(self, **_operators):
        """ Exclude one OR many <expression> or <operator:expression> from search

        Optional keyword arguments:
            - expression        --  -expression
            - indexed           --  -site:domain.tld
            - in_title          --  -intitle:expression
            - filetype          --  -filetype:ext
        """

        self._add_commands(exclude=True, **_operators)
        return self

    def to(self, cls, location=Location.WORLDWIDE):
        return cls(self, tld=location)

    def to_google(self, location=Location.WORLDWIDE):
        return self.to(GoogleRequest, location)

    def to_bing(self, location=Location.WORLDWIDE):
        return self.to(BingRequest, location)
