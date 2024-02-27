from python_advanced_search.models.commands import Command
from python_advanced_search.engines.bing.commands.operators import (
    IndexedUrlOperator,
    InTextOperator,
    LocationOperator,
    LanguageOperator,
    LinkFromDomainOperator,
    LinkDomainOperator,
)


class IndexedUrlCommand(Command):
    """
    Instance of IndexedUrlOperator (Bing operator) with <searched value>

    Command is equal to <url:value>
        :param Expression expression: can be "exact" or simple expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=IndexedUrlOperator(exclude)
        )


class InBodyCommand(Command):
    """
    Instance of InTextOperator (Bing operator) with <searched value>

    Command is equal to <inbody:value>
        :param Expression expression: can be "exact" or simple expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=InTextOperator(exclude)
        )


class LocationCommand(Command):
    """
    Instance of LocationOperator (Bing operator) with <searched value>

    Command is equal to <location:value>
        :param Expression expression: can be "exact" or simple expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=LocationOperator(exclude)
        )


class LanguageCommand(Command):
    """
    Instance of LanguageOperator (Bing operator) with <searched value>

    Command is equal to <language:value>
        :param Expression expression: can be "exact" or simple expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=LanguageOperator(exclude)
        )


class LinkFromDomainCommand(Command):
    """
    Instance of LinkFromDomainOperator (Bing operator) with <searched value>

    Command is equal to <linkfromdomain:value>
        :param Expression expression: can be "exact" or simple expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=LinkFromDomainOperator(exclude)
        )


class LinkDomainCommand(Command):
    """
    Instance of LinkDomainOperator (Bing operator) with <searched value>

    Command is equal to <linkdomain:value>
        :param Expression expression: can be "exact" or simple expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=LinkDomainOperator(exclude)
        )
