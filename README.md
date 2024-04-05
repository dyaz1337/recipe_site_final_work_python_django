## Для установки Django выполним команду:
- pip install django

## Создание первого проекта

- django-admin startproject recipes

*** Далее переходим в каталог проекта командой:
- cd recipes

*** Запускаем проект (остановить Ctrl+C):
- python manage.py runserver

*** Создание первого приложения в Django представляет собой создание
отдельного модуля, который будет содержать логику и шаблоны для определенной функциональности.
 
- python manage.py startapp recipesapp

*** Добавление приложения в проект
Чтобы добавить созданное приложение в проект, необходимо указать его в настройках проекта (файл settings.py). Для этого нужно добавить название приложения в список INSTALLED_APPS.
Внимание! Хорошей привычкой будет делать два действия сразу друг за другом. А именно создавать приложение через startapp и сразу добавляет его в список INSTALLED_APPS.
Учитывая добавленные по умолчанию приложения, константа 
- INSTALLED_APPS будет выглядет так: INSTALLED_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'recipesapp', ]

*** Далее добавим админку сайта 
- в начале надо применить миграции
- python manage.py migrate  
- далее создаем суперпользователя
- python manage.py createsuperuser 
- Имя пользователя (leave blank to use 'misha'): user
* Адрес электронной почты: user@mail.ru
* Password: 
* Password (again):
* Superuser created successfully.
