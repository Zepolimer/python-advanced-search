from python_advanced_search.models.commands.operators import Operator


class IndexedUrlOperator(Operator):
    """
    Bing operator <url:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='url:',
            exclude=exclude
        )


class InTextOperator(Operator):
    """
    Bing operator <inbody:> similar to <intext:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='inbody:',
            exclude=exclude
        )


class LocationOperator(Operator):
    """
    Bing operator <location:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='location:',
            exclude=exclude
        )


class LanguageOperator(Operator):
    """
    Bing operator <language:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='language:',
            exclude=exclude
        )


class LinkFromDomainOperator(Operator):
    """
    Bing operator <linkfromdomain:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='linkfromdomain:',
            exclude=exclude
        )


class LinkDomainOperator(Operator):
    """
    Bing operator <linkdomain:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='linkdomain:',
            exclude=exclude
        )
