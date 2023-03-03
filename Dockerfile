FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "main.py", "run-bot"]
