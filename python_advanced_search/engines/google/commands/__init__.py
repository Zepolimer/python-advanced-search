from python_advanced_search.models.commands import Command
from python_advanced_search.engines.google.commands.operators import (
    AllInTitleOperator,
    InTextOperator,
    AllInTextOperator,
    InUrlOperator,
    AllInUrlOperator,
    InAnchorOperator,
    AllInAnchorOperator,
    DefineOperator,
    RelatedOperator
)


class AllInTitleCommand(Command):
    """
    Instance of AllInTitleOperator (Google operator) with <searched value>

    Command is equal to <allintitle:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=AllInTitleOperator(exclude)
        )


class InTextCommand(Command):
    """
    Instance of InTextCommand (Google operator) with <searched value>

    Command is equal to <intext:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=InTextOperator(exclude)
        )


class AllInTextCommand(Command):
    """
    Instance of AllInTextOperator (Google operator) with <searched value>

    Command is equal to <allintext:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=AllInTextOperator(exclude)
        )


class InUrlCommand(Command):
    """
    Instance of InUrlOperator (Google operator) with <searched value>

    Command is equal to <inurl:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=InUrlOperator(exclude)
        )


class AllInUrlCommand(Command):
    """
    Instance of AllInUrlOperator (Google operator) with <searched value>

    Command is equal to <allinurl:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=AllInUrlOperator(exclude)
        )


class InAnchorCommand(Command):
    """
    Instance of InAnchorOperator (Google operator) with <searched value>

    Command is equal to <inanchor:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=InAnchorOperator(exclude)
        )


class AllInAnchorCommand(Command):
    """
    Instance of AllInAnchorOperator (Google operator) with <searched value>

    Command is equal to <allinanchor:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=AllInAnchorOperator(exclude)
        )


class RelatedCommand(Command):
    """
    Instance of RelatedOperator (Google operator) with <searched value>

    Command is equal to <related:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=RelatedOperator(exclude)
        )


class DefineCommand(Command):
    """
    Instance of DefineOperator (Google operator) with <searched value>

    Command is equal to <define:value>
        :param Expression expression: can be "exact" or simple
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=DefineOperator(exclude)
        )
