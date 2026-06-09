# Входной аудит проекта Feedback System

## 1. Текущая структура
- **Backend:** Flask, SQLAlchemy (SQLite), Flask-Login.
- **Интерфейс:** Шаблоны Jinja2 + Bootstrap 5.
- **Данные:** Таблицы `categories` и `feedback`.

## 2. Технический долг и план доработки
- [ ] Перенос чувствительных данных (SECRET_KEY) в `.env`.
- [ ] Контейнеризация (Dockerfile/Compose) — *в работе (Этап 2)*.
- [ ] Настройка CI/CD (GitHub Actions) — *в работе (Этап 6)*.
- [ ] Реализация Unit-тестирования — *в работе (Этап 4)*.

## 3. Стек технологий
- Python 3.10+
- Flask 2.x
- SQLAlchemy
- Gunicorn (для деплоя)