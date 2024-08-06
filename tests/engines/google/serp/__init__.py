import unittest

from python_advanced_search.engines.google.serp import GoogleSerpAnalyzer


class GoogleSerpTestCase(unittest.TestCase):
    def test_serp(self):
        with open('tests/engines/google/serp/index.html', 'r') as f:
            analyzer = GoogleSerpAnalyzer(f.read())
            serp = analyzer.get_serp()

            self.assertEqual(
                serp.nb_results,
                23500000
            )
            self.assertEqual(
                serp.title,
                'python unittest - Recherche Google'
            )

            self.assertEqual(len(serp.links), 7)

            link = serp.links[0]
            self.assertEqual(
                link.title,
                'Les tests unitaires automatisés avec unittest — Python 3.X'
            )
            self.assertEqual(
                link.url,
                'https://gayerie.dev/docs/python/python3/unittest.html'
            )

            link = serp.links[1]
            self.assertEqual(
                link.title,
                'Ajoutez des tests avec Unittest - Testez votre projet Python'
            )
            self.assertEqual(
                link.url,
                'https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python/7414161-ajoutez-des-tests-avec-unittest'
            )

            link = serp.links[2]
            self.assertEqual(
                link.title,
                'unittest — Framework de tests unitaires'
            )
            self.assertEqual(
                link.url,
                'https://docs.python.org/fr/3.8/library/unittest.html'
            )

            link = serp.links[3]
            self.assertEqual(
                link.title,
                'Getting Started With Testing in Python'
            )
            self.assertEqual(
                link.url,
                'https://realpython.com/python-testing/'
            )

            link = serp.links[4]
            self.assertEqual(
                link.title,
                'Unit Testing with Python unittest Module'
            )
            self.assertEqual(
                link.url,
                'https://geekflare.com/unit-testing-with-python-unittest/'
            )

            link = serp.links[5]
            self.assertEqual(
                link.title,
                'A Beginner\'s Guide to Unit Tests in Python (2023)'
            )
            self.assertEqual(
                link.url,
                'https://www.dataquest.io/blog/unit-tests-python/'
            )

            link = serp.links[6]
            self.assertEqual(
                link.title,
                'A Gentle Introduction to Unit Testing in Python'
            )
            self.assertEqual(
                link.url,
                'https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/'
            )
