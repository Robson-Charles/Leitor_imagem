FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install flask

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0"]
