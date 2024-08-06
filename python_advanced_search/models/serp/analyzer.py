import abc

from lxml.html import document_fromstring

from python_advanced_search.models.serp import Serp


class SerpAnalyzer:
    def __init__(self, html):
        self.html = html
        self.document = document_fromstring(self.html)
        self.serp = Serp()

    @abc.abstractmethod
    def get_serp(self):
        """ This method must be implemented"""