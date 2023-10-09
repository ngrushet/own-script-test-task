FROM python:3.9

# Установите переменную окружения PYTHONUNBUFFERED в значение 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ls -a