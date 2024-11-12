from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from title_page.views import method

class HomePageTest(TestCase):
    '''Homepage test'''
    def test_home_page(self):
        '''modul test for home page'''
        found = resolve('/')
        self.assertEqual(found.func, method)
    def test_home_page_correct_return(self):
        """test: home page returns correct html page"""
        request = HttpRequest()
        response = method(request)
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn(r"<h1>Hello, world. You're at the polls index.</h1>", html)
        self.assertTrue(html.endswith('</html>'))