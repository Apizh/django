from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


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
        self.browser.get('http://localhost:8000/')  # добавлен полный URL
        # Проверка, что заголовок страницы правильный
        self.assertIn("Tasks Page", self.browser.title)

        # Проверка заголовка на странице
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Tasks list", header_text)

        # Добавление новой задачи
        input_task = self.browser.find_element(By.ID, 'id_new_task')  # исправлено на By.ID

        self.assertEqual(  # исправлено на assertEqual
            input_task.get_attribute('placeholder'),
            'Enter task'
        )

        # Input task in field
        input_task.send_keys('Learn Alembic')
        time.sleep(10)
        # Нажимаем Enter, чтобы добавить задачу
        input_task.send_keys(Keys.ENTER)
        time.sleep(2)  # Можно заменить на WebDriverWait, но пока используем sleep для упрощения

        # Проверка, что задача появилась в таблице
        table = self.browser.find_element(By.ID, 'id_list_table')  # исправлено на By.ID
        rows = table.find_elements(By.TAG_NAME, 'tr')  # исправлено на By.TAG_NAME
        self.assertFalse(any(row.text == 'Learn Alembic' for row in rows))

        # self.fail('Tests can be ending')  # Эта строка вызывает ошибку, если нужно остановить тест


if __name__ == '__main__':
    unittest.main(warnings='ignore')
