from selenium import webdriver
from unittest import TestCase
import unittest


class TestVisitor(TestCase):
    '''Testing new visitor'''

    def setUp(self):
        '''Pre install'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''Close browser'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''Test can be started'''
        self.browser.get('localhost:8000/')
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        self.assertIn("Hello, world. You're at the polls index.", self.browser.page_source)
        #self.fail('Tests can be ending')


if __name__ == '__main__':
    unittest.main(warnings='ignore')