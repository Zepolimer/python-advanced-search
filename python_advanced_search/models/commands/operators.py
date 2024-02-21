class Operator:
    """
    Base Operator
        :param str name: search engine operator
        :param bool exclude: False by default, if True add a '-' before <name>
    """

    def __init__(self, name, exclude=False):
        self.__name = name
        if exclude:
            self.__name = '-%s' % name

    def __str__(self):
        return self.__name


class AndOperator(Operator):
    """ Conditional operator <AND> """

    def __init__(self):
        super().__init__(name='AND')


class NotOperator(Operator):
    """ Conditional operator <NOT> """

    def __init__(self):
        super().__init__(name='NOT')


class OrOperator(Operator):
    """ Conditional operator <OR> """

    def __init__(self):
        super().__init__(name='OR')


class IndexedOperator(Operator):
    """
    Common operator <site:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='site:',
            exclude=exclude
        )


class InTitleOperator(Operator):
    """
    Common operator <intitle:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='intitle:',
            exclude=exclude
        )


class FiletypeOperator(Operator):
    """
    Common operator <filetype:>
        :param bool exclude: False by default
    """

    def __init__(self, exclude=False):
        super().__init__(
            name='filetype:',
            exclude=exclude
        )
