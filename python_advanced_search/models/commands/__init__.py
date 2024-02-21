from python_advanced_search.models.commands.operators import (
    Operator,
    IndexedOperator,
    InTitleOperator,
    FiletypeOperator,
)
from python_advanced_search.models.commands.expressions import Expression, E


class Command:
    """
    Command class combines Operator and Expression, ExactExpression classes
        :param Expression expression: Expression or ExactExpression instance
        :param Operator operator: None or Operator instance (or subclass)
    """

    def __init__(self, expression, operator=None):
        self.str = expression.value

        if operator is not None and isinstance(operator, Operator):
            self.str = '%s%s' % (operator, expression)


class ExpressionCommand(Command):
    """
    <expression> (simple expression)
        :param Expression expression: expression
        :param bool exclude: False by default
    """
    def __init__(self, expression, exclude=False):
        # self.expression = Expression(expression, exclude)
        super().__init__(
            expression=expression
        )


class ExactExpressionCommand(Command):
    """
    <"expression"> (exact expression)
        :param str expression: expression
        :param bool exclude: False by default
    """
    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=E(expression, exclude)
        )


class IndexedCommand(Command):
    """
    <site:expression>
        :param Expression expression: expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=IndexedOperator(exclude),
        )


class InTitleCommand(Command):
    """
    <intitle:expression>
        :param Expression expression: expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=InTitleOperator(exclude),
        )


class FiletypeCommand(Command):
    """
    <filetype:expression>
        :param Expression expression: expression
        :param bool exclude: False by default
    """

    def __init__(self, expression, exclude=False):
        super().__init__(
            expression=expression,
            operator=FiletypeOperator(exclude),
        )
