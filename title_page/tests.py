from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from title_page.models import Item
from title_page.views import index


class HomePageTest(TestCase):
    '''Homepage test'''

    def test_home_page(self):
        '''Test: home page'''
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_correct_htm(self):
        """Test: home page returns correct html page"""
        response = self.client.get('/')
        html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn("<h1>Tasks list.</h1>", html)
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'index.html')

    def test_can_save_POST_request(self):
        '''Test: Make safe post-request'''
        response = self.client.post('/', data={'item_text': 'New list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "New list item")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        self.assertNotIn('New list item', response.content.decode('utf-8'))
        #self.assertTemplateUsed(response, 'index.html')

    def test_only_saves_items_when_necessary(self):
        """Тест: сохраняет элементы только когда нужно"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    '''Тест модели элемента списка'''

    def test_saving_and_retrieving_items(self):
        '''Тест сохранения и получения элементов списка'''
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "The second item"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "The second item")
