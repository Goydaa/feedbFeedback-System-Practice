# Используем легкий Python
FROM python:3.10-slim

# Рабочая директория
WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Открываем порт 5000
EXPOSE 5000

# Команда запуска
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]