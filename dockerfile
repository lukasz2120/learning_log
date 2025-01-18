FROM python:3.10-slim

WORKDIR /usr/src/app

# Ustawienie zmiennej środowiskowej, aby Python nie buforował wyjścia (dla logów)
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

