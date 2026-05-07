#в нашем проектк через него джанго узнает где лежат настройки проекта
import os
#подключаем модуль sys, нужен чтобы джанго мог считать команды из терминала
import sys


#создаем функцию мейн - главная функция для управления проекта
def main():
    #эта страка говорит джанго что настройки проекта лежат в config/settings.py
    #DJANGO_SETTINGS_MODULE - специальная переменная джанго
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    #импортируем специальную переменую джанго умеющюю выполнять команды из терминала
    from django.core.management import execute_from_command_line
    #строка запускает команду котрую мы записали в теринале
    execute_from_command_line(sys.argv)

#проверяем тот ли файл мейн мы запустили напрямую
if __name__ == '__main__':
    main()