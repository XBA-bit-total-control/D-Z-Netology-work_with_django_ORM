## Выполнение задания с каталогом товаров в директории 'main'

## Онлайн библиотека в директории 'models_list_displaying'


Для запуска проекта нужно:

Установить библиотеки из requirements.txt:

```bash
pip install -r requirements.txt
```

После следующие команды выполнить:

- Создания миграций приложения для базы данных

```bash
python manage.py migrate
```

- Запуск сервера

```bash
python manage.py runserver
```

- Для загрузки данных в БД - команда:
    для 'main'
```bash
python manage.py manage.py import_phones
```

- Для загрузки данных в БД - команда:
    для 'models_list_displaying'
```bash
python manage.py manage.py download_data
```