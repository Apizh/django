from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from title_page.views import index


class HomePageTest(TestCase):
    '''Homepage test'''

    def test_home_page(self):
        '''modul test for home page'''
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_correct_htm(self):
        """test: home page returns correct html page"""
        response = self.client.get('/')
        html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn("<h1>Tasks list.</h1>", html)
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'index.html')