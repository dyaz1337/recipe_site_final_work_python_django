# Проект “Сайт рецептов” на Django

Данный проект является реализацией итоговой аттестации по программе
“Вебразработка на Python” и представляет собой веб-приложение
для хранения и просмотра рецептов. 
Пользователи могут добавлять, просматривать и редактировать рецепты, 
а также просматривать рецепты других пользователей.

## Установка
1. Клонируйте репозиторий на ваше устройство:

    ```bash
    git clone [https://github.com/dyaz1337/recipe_site_final_work_python_django]
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Создайте базу данных MySQL и настройте соединение с базой данных в файле settings.py:

    ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_name$default',
        'USER': 'your_name',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'your_name.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
   ```
   
   Или можете раскомментировать следующие строки для работы с sqlite3 (и удалить строки ниже до блока `# Password validation`):
   ```python
   DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
   }
   ```
   
4. Примените миграции базы данных:

    ```bash
    python manage.py migrate
    ```

5. Для создания суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки Django:

    ```bash
    python manage.py runserver
    ```

7. Откройте ваш веб-браузер и перейдите по адресу http://localhost:8000/, чтобы начать использование приложения.

## Функции

- Регистрация и аутентификация пользователей
- Просмотр главной страницы с 3 рецептами кратко
- Просмотр подробной информации о рецепте
- Добавление, редактирование рецептов
- Возможность добавления изображения для рецепта
- Категоризация рецептов

## Технологии

- Python
- Django - фреймворк для разработки веб-приложений
- MySQL - СУБД для хранения данных
- HTML/CSS - для создания пользовательского интерфейса

## Проект развернут по адресу : 

[https://dyaz.pythonanywhere.com/]
