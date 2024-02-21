class Expression:
    """
    Return a <searched expression>
        :param str value: keyword or string
        :param bool exclude: False by default
    """

    def __init__(self, value, exclude=False):
        self.value = value
        if exclude:
            self.value = '-%s' % value

    def __str__(self):
        return self.value

    def exclude(self):
        self.value = '-%s' % self.value


class E(Expression):
    """
    Return a <"searched expression"> using double quotes
        :param str value: keyword or string
        :param bool exclude: False by default, if implemented add an '-' before <value>
    """

    def __init__(self, value, exclude=False):
        super().__init__('"%s"' % value, exclude)
