import unittest

from python_advanced_search.engines.bing.serp import BingSerpAnalyzer


class BingSerpTestCase(unittest.TestCase):
    def test_serp(self):
        with open('tests/engines/bing/serp/index.html', 'r') as f:
            analyzer = BingSerpAnalyzer(f.read())
            serp = analyzer.get_serp()

            self.assertEqual(
                serp.nb_results,
                5980000
            )

            self.assertEqual(
                serp.title,
                'python unittest - Search'
            )

            self.assertEqual(len(serp.links), 10)

            link = serp.links[0]
            self.assertEqual(
                link.title,
                "unittest — Unit testing framework — Python 3.12.3 documentation"
            )
            self.assertEqual(
                link.url,
                "https://docs.python.org/3/library/unittest.html"
            )

            link = serp.links[1]
            self.assertEqual(
                link.title,
                "Python's unittest: Writing Unit Tests for Your Code"
            )
            self.assertEqual(
                link.url,
                "https://realpython.com/python-unittest"
            )

            link = serp.links[2]
            self.assertEqual(
                link.title,
                "Introduction to Python unittest Framework - Python Tutorial"
            )
            self.assertEqual(
                link.url,
                "https://www.pythontutorial.net/python-unit-testing/python-unittestpython-tutorials.indata-flair.training"
            )

            link = serp.links[3]
            self.assertEqual(
                link.title,
                "Getting Started With Testing in Python – Real Python"
            )
            self.assertEqual(
                link.url,
                "https://realpython.com/python-testing"
            )

            link = serp.links[4]
            self.assertEqual(
                link.title,
                "Ajoutez des tests avec Unittest - Testez votre projet Python ..."
            )
            self.assertEqual(
                link.url,
                "https://openclassrooms.com/.../7414161-ajoutez-des-tests-avec-un…"
            )

            link = serp.links[5]
            self.assertEqual(
                link.title,
                "A Beginner’s Guide to Unit Tests in Python (2023) - Dataquest"
            )
            self.assertEqual(
                link.url,
                'https://www.dataquest.io/blog/unit-tests-pyt'
            )

            link = serp.links[6]
            self.assertEqual(
                link.title,
                "Unit Testing in Python Tutorial | DataCamp"
            )
            self.assertEqual(
                link.url,
                "https://www.datacamp.com/tutorial/unit-t…"
            )
