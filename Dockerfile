# Используем alpine, но добавляем необходимые инструменты для сборки
FROM python:3.12-alpine

# Запрещаем Python писать файлы .pyc на диск и включаем буферизацию логов
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Устанавливаем системные зависимости для PostgreSQL и сборки библиотек
RUN apk add --no-cache postgresql-dev gcc musl-dev libffi-dev

# Сначала копируем только зависимости
COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Теперь копируем всё остальное (этот слой будет меняться часто)
COPY . .

# Запускаем через uvicorn 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]