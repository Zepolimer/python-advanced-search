import unittest
from unittest.mock import Mock, patch

from python_advanced_search.services.crawler import GoogleRequest, Response, Request
from python_advanced_search.models.query import Query
from python_advanced_search.models.commands.conditions import OR, NOT, AND
from python_advanced_search.models.commands.expressions import E
from python_advanced_search.services.serp import GoogleSerpAnalyzer


class QueryTestCase(unittest.TestCase):
    # def test_query_expression(self):
    #     query = Query()
    #     query.include(expression='expression')
    #
    #     self.assertEqual(query.str, 'expression')
    #     self.assertEqual(
    #         query.encoded_str,
    #         'q=expression'
    #     )
    #
    # def test_query(self):
    #     query = Query()
    #     query.include(
    #         indexed='mywebsite.com',
    #         in_title=E('seo'),
    #     ).exclude(
    #         indexed='excluded-website.com'
    #     )
    #
    #     self.assertEqual(
    #         query.str,
    #         'site:mywebsite.com intitle:"seo" -site:excluded-website.com'
    #     )
    #     self.assertEqual(
    #         query.encoded_str,
    #         'q=site%3Amywebsite.com+intitle%3A%22seo%22+-site%3Aexcluded-website.com'
    #     )
    #
    # def test_query_conditions(self):
    #     query = Query()
    #     query.include(
    #         indexed=AND('first-and.com', 'second-and.io'),
    #         in_title=OR('title_1', 'title_2', 'title_3'),
    #         filetype=NOT('pdf', 'png')
    #     )
    #
    #     self.assertEqual(
    #         query.str,
    #         'site:(first-and.com AND second-and.io) intitle:(title_1 OR title_2 OR title_3) filetype:(pdf NOT png)'
    #     )
    #     self.assertEqual(
    #         query.encoded_str,
    #         'q=site%3A%28first-and.com+AND+second-and.io%29+intitle%3A%28title_1+OR+title_2+OR+title_3%29+filetype%3A%28pdf+NOT+png%29'
    #     )

    def test_query_crawler(self):

        mock_content = Mock()
        mock_content.return_value = (
            """
                <html></html>
            """
        )

        mock_page = Mock()
        mock_page.return_value = Mock(
            content=mock_content,
        )

        mock_playwright = Mock()
        mock_playwright.start().chromium.launch().new_context().new_page = mock_page

        with patch('python_advanced_search.services.crawler.sync_playwright', return_value=mock_playwright):
            request = Query().include(
                expression='tapis bleu'
            ).to(GoogleRequest)

            response = request.get()
            print(request.target_url)
            print(response.__dict__)

        # serp = GoogleSerpAnalyzer(response.html).get_serp()
        # self.assertEqual(
        #     serp.nb_results,
        #     78500000
        # )
        # self.assertEqual(
        #     serp.title,
        #     'title : tapis bleu - Recherche Google'
        # )
        #
        # for link in serp.links:
        #     print('link.title : %s' % link.title)
        #     print('link.url : %s' % link.url)

        # for b in serp.blocks:
        #     if isinstance(b, SimilarRequestBlock):
        #         print('block : %s' % b.requests)

