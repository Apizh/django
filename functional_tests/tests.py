from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


class TestVisitor(LiveServerTestCase):
    '''Testing new visitor'''

    def setUp(self):
        '''Pre install'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''Close browser'''
        self.browser.quit()

    def check_for_row_in_list(self, row_text):
        '''подтверждение строки в таблице списка'''
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''Test can be started'''
        self.browser.get(self.live_server_url)  # добавлен полный URL
        # Проверка, что заголовок страницы правильный
        self.assertIn("Tasks Page", self.browser.title)

        # Проверка заголовка на странице
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Tasks list", header_text)

        # Добавление новой задачи
        input_task = self.browser.find_element(By.ID, 'id_new_task')  # исправлено на By.ID
        # Input task in field
        input_task.send_keys('Learn Alembic')
        # Нажимаем Enter, чтобы добавить задачу
        input_task.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Learn Alembic')
        input_task = self.browser.find_element(By.ID, 'id_new_task')  # Снова находим поле ввода
        input_task.send_keys('Alembic')
        input_task.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('2: Alembic')
        # time.sleep(2) Можно заменить на WebDriverWait, но пока используем sleep для упрощения

    def wait_for_row_in_list_table(self, row_text):
        """Ожидать строку в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')  # исправлено на By.ID
                rows = table.find_elements(By.TAG_NAME, 'tr')  # исправлено на By.TAG_NAME
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    # self.fail('Tests can be ending')  # Эта строка вызывает ошибку, если нужно остановить тест
