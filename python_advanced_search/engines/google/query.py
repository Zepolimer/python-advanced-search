from python_advanced_search.models.query import Query


class GoogleQuery(Query):
    _operators = [
        'all_in_title',
        'in_text',
        'all_in_text',
        'in_url',
        'all_in_url',
        'in_anchor',
        'all_in_anchor',
        'related',
        'define',
    ]

    def include(self, **_operators):
        """
        Optional keyword arguments:
            - expression        --  (expression)
            - exact_expression  --  ("expression")
            - indexed           --  (site:domain.tld)
            - in_title          --  (intitle:expression)
            - all_in_title      --  (allintitle:expression)
            - in_text           --  (intext:expression)
            - all_in_text       --  (allintext:expression)
            - in_url            --  (inurl:url)
            - all_in_url        --  (allinurl:url)
            - in_anchor         --  (inanchor:expression)
            - all_in_anchor     --  (allinanchor:expression)
            - related           --  (related:domain.tld)
            - define            --  (define:expression)
            - filetype          --  (filetype:ext)
        """

        self._add_commands(**_operators)
        return self

    def exclude(self, **_operators):
        """
        Optional keyword arguments:
            - expression        --  (-expression)
            - exact_expression  --  (-"expression")
            - indexed           --  (-site:domain.tld)
            - in_title          --  (-intitle:expression)
            - all_in_title      --  (-allintitle:expression)
            - in_text           --  (-intext:expression)
            - all_in_text       --  (-allintext:expression)
            - in_url            --  (-inurl:url)
            - all_in_url        --  (-allinurl:url)
            - in_anchor         --  (-inanchor:expression)
            - all_in_anchor     --  (-allinanchor:expression)
            - related           --  (-related:domain.tld)
            - define            --  (-define:expression)
            - filetype          --  (-filetype:ext)
        """

        self._add_commands(exclude=True, **_operators)
        return self
