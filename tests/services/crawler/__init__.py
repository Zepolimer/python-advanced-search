import unittest
from unittest.mock import Mock, patch

from python_advanced_search.services.crawler import GoogleRequest
from python_advanced_search.models.query import Query


class CrawlerTestCase(unittest.TestCase):
    def test_request(self):
        mock_content = Mock()
        mock_content.return_value = '<html></html>'

        mock_page = Mock()
        mock_page.return_value = Mock(
            content=mock_content
        )

        mock_playwright = Mock()
        mock_playwright.start().chromium.launch().new_context().new_page = mock_page

        with patch('python_advanced_search.services.crawler.sync_playwright', return_value=mock_playwright):
            request = Query().include(
                expression='python unittest'
            ).to(GoogleRequest)

            response = request.get()

            self.assertEqual(
                response.html,
                '<html></html>'
            )
