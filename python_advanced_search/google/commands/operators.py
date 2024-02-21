from python_advanced_search.models.commands.operators import Operator


class AllInTitleOperator(Operator):
    """
    Google operator <allintitle:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='allintitle:',
            exclude=exclude
        )


class InTextOperator(Operator):
    """
    Google operator <intext:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='intext:',
            exclude=exclude
        )


class AllInTextOperator(Operator):
    """
    Google operator <allintext:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='allintext:',
            exclude=exclude
        )


class InUrlOperator(Operator):
    """
    Google operator <inurl:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='inurl:',
            exclude=exclude
        )


class AllInUrlOperator(Operator):
    """
    Google operator <allinurl:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='allinurl:',
            exclude=exclude
        )


class InAnchorOperator(Operator):
    """
    Google operator <inanchor:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='inanchor:',
            exclude=exclude
        )


class AllInAnchorOperator(Operator):
    """
    Google operator <allinanchor:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='allinanchor:',
            exclude=exclude
        )


class RelatedOperator(Operator):
    """
    Google operator <related:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='related:',
            exclude=exclude
        )


class DefineOperator(Operator):
    """
    Google operator <define:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='define:',
            exclude=exclude
        )
