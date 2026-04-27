FROM python:3.14-bookworm

WORKDIR /home/flaskApp

COPY requirements.txt .
COPY ./app /home/flaskApp/app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "-w", "4", "app.wsgi:app"]