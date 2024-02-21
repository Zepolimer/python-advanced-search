from python_advanced_search.models.commands.expressions import Expression
from python_advanced_search.models.commands.operators import (
    OrOperator,
    AndOperator,
    NotOperator
)


class Q:
    def __init__(self, operator, *args, **kwargs):
        """
        Base for conditions classes : add expressions (args) to query
            :param operator: Operator
            :param args: Expression and / or E (ExactExpression)
        """
        operator_name = ' %s ' % operator

        self.expressions = []
        for arg in args:
            self.expressions.append(arg)

        self.expression = Expression(operator_name.join(self.expressions))
        self.value = '(%s)' % self.expression.value

    def __str__(self):
        return '(%s)' % self.expression.value


class OR(Q):
    OPERATOR = OrOperator()

    def __init__(self, *args, **kwargs):
        super().__init__(self.OPERATOR, *args, **kwargs)


class AND(Q):
    OPERATOR = AndOperator()

    def __init__(self, *args, **kwargs):
        super().__init__(self.OPERATOR, *args, **kwargs)


class NOT(Q):
    OPERATOR = NotOperator()

    def __init__(self, *args, **kwargs):
        super().__init__(self.OPERATOR, *args, **kwargs)
