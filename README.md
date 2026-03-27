# Магистерская программа "Финансовая экономика и бизнес-аналитика"

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django)
![DRF](https://img.shields.io/badge/DRF-3.14-a30f2d?style=for-the-badge&logo=django)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker)

Веб-приложение для презентации магистерской программы РГУ им. А.Н. Косыгина. Проект разработан в рамках учебного портфолио.

## 🚀 Функциональность

### Публичная часть
- **Главная страница**: Информация о программе, преимущества, статистика.
- **О программе**: Детальное описание учебного процесса.
- **FAQ**: Ответы на часто задаваемые вопросы (аккордеон).
- **Контакты**: Форма обратной связи для абитуриентов.
- **Локализация**: Поддержка русского языка (базовая настройка i18n).

### Личный кабинет
- **Регистрация/Вход**: Аутентификация пользователей (без email-подтверждения).
- **Профиль**: Редактирование личных данных, загрузка аватара.
- **Мои заявки**: Просмотр истории отправленных заявок.

### API
- **REST API**: Полный доступ к данным через API.
- **Swagger/Redoc**: Автогенерируемая документация (`/api/docs/`).
- **JWT Auth**: Аутентификация по токенам для внешних клиентов.

## 🛠 Технологический стек

- **Backend**: Python 3.9+, Django 4.2 LTS
- **API**: Django Rest Framework, drf-spectacular (OpenAPI 3.0)
- **Auth**: SimpleJWT (JWT), Session Auth
- **Database**: SQLite (для разработки)
- **Frontend**: Django Templates, HTML5, CSS3, Vanilla JS
- **DevOps**: Docker

## 📦 Установка и запуск

### Локальный запуск (без Docker)

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/bukabtw/master-finance-rguk.git
   cd master-finance-rguk
   ```

2. **Создайте и активируйте виртуальное окружение**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции**
   ```bash
   python manage.py migrate
   ```

5. **Создайте суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер**
   ```bash
   python manage.py runserver
   ```
   Сайт доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Запуск в Docker

1. **Соберите образ**
   ```bash
   docker build -t master-finance .
   ```

2. **Запустите контейнер**
   ```bash
   docker run -p 8000:8000 -v "%cd%/media:/app/media" master-finance
   ```
   *Примечание: `-v` используется для сохранения загруженных медиа-файлов (аватарок).*

## 📚 API Документация

Документация доступна после запуска сервера:
- **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **Redoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- **Schema JSON**: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

## 📂 Структура проекта

```
master-finance-rguk/
├── config/             # Настройки проекта
├── core/               # Основной функционал (страницы, заявки)
├── users/              # Пользователи и аутентификация
├── static/             # Статические файлы (CSS, JS, Images)
├── media/              # Медиа файлы (загружаемые пользователями)
├── templates/          # HTML шаблоны
├── manage.py
├── requirements.txt
└── Dockerfile
```
