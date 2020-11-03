# ЗАДАНИЕ 1:
# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os, sys

# Функция создания папок
def dir_spawner(dir_name='dir', dir_count=9):   # Дефолтные арги - имя папки и количество
    for i in range(1, dir_count + 1):   # Цикл создания
        # Чтобы папки создавались именно в папке расположения модуля,
        # а не в cwd, для создания пути через os.path.join используется
        # os.path.dirname - эта функция возвращает только имя директории от расположения
        # текущего файла (берется из sys.argv[0]):
        new_path = os.path.join(os.path.dirname(sys.argv[0]), f'{dir_name}_{i}')
        # Cобственно создание папки:
        os.mkdir(new_path)

# Функция удаления папок. Тот же принцип действия
def dir_killer(dir_name='dir', dir_count=9):
    for i in range(1, dir_count + 1):
        new_path = os.path.join(os.path.dirname(sys.argv[0]), f'{dir_name}_{i}')
        os.rmdir(new_path)


# dir_spawner()
# dir_killer()
