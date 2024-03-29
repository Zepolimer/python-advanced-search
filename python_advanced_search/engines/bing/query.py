from python_advanced_search.models.query import Query


class BingQuery(Query):
    _operators = [
        'url',
        'in_body',
        'location',
        'language',
        'link_from_domain',
        'link_domain',
    ]

    def include(self, **_operators):
        """
        Optional keyword arguments:
            - url               --  (url:domain.tld)
            - in_body           --  (inbody:expression)
            - location          --  (location:expression)
            - language          --  (language:url)
            - link_from_domain  --  (linkfromdomain:url)
            - link_domain       --  (link_domain:expression)
        """

        self._add_commands(**_operators)
        return self

    def exclude(self, **_operators):
        """
        Optional keyword arguments:
            - url               --  (-url:domain.tld)
            - in_text           --  (-inbody:expression)
            - location          --  (-location:expression)
            - language          --  (-language:url)
            - link_from_domain  --  (-linkfromdomain:url)
            - link_domain       --  (-link_domain:expression)
        """

        self._add_commands(exclude=True, **_operators)
        return self

    def search(self):
        return self.to_bing()
