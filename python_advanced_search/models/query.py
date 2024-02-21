from python_advanced_search.models.commands.expressions import Expression, E
from python_advanced_search.models.commands import (
    ExpressionCommand,
    ExactExpressionCommand,
    IndexedCommand,
    InTitleCommand,
    FiletypeCommand,
)


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
        self.str = ''

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

    def _join_commands(self):
        query = []
        for command in self.commands:
            query.append(command.str)

        self.str = ' '.join(query)

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

        if len(self.commands) > 0:
            self._join_commands()

    def search(self, **_operators):
        """ Search for one OR many <expression> or <operator:expression>

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
