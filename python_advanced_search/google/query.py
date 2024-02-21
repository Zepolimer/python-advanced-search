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

    def search(self, **_operators):
        """
        Optional keyword arguments:
            - expression        --  (expression)
            - exact_expression  --  ("expression")
            - indexed           --  (site:domain.tld)
            - in_title          --  (intitle:expression)
            - all_in_title      --  (all_in_title:expression)
            - in_text           --  (in_text:expression)
            - all_in_text       --  (all_in_text:expression)
            - in_url            --  (in_url:url)
            - all_in_url        --  (all_in_url:url)
            - in_anchor         --  (in_anchor:expression)
            - all_in_anchor     --  (all_in_anchor:expression)
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
            - all_in_title      --  (-all_in_title:expression)
            - in_text           --  (-in_text:expression)
            - all_in_text       --  (-all_in_text:expression)
            - in_url            --  (-in_url:url)
            - all_in_url        --  (-all_in_url:url)
            - in_anchor         --  (-in_anchor:expression)
            - all_in_anchor     --  (-all_in_anchor:expression)
            - related           --  (-related:domain.tld)
            - define            --  (-define:expression)
            - filetype          --  (-filetype:ext)
        """

        self._add_commands(exclude=True, **_operators)
        return self
