from selenium import webdriver

test1 = webdriver.Firefox()
# Эдит слышала про крутое новое онлайн-приложение со списком
# неотложных дел. Она решает оценить его домашнюю страницу
test1.get("localhost:8000/admin")
# Она видит, что заголовок и шапка страницы говорят о списках
# неотложных дел
assert 'To-do' in test1.title

# Ей сразу же предлагается ввести элемент списка
# Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби –
# вязание рыболовных мушек)
# Когда она нажимает enter, страница обновляется, и теперь страница
# содержит "1: Купить павлиньи перья" в качестве элемента списка
# Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
# Она вводит "Сделать мушку из павлиньих перьев"
# (Эдит очень методична)
# Страница снова обновляется, и теперь показывает оба элемента ее списка
# Эдит интересно, запомнит ли сайт ее список. Далее она видит, что
# сайт сгенерировал для нее уникальный URL-адрес – об этом
# выводится небольшой текст с объяснениями.
# Она посещает этот URL-адрес – ее список по-прежнему там.
test1.quit()
