FROM python:3.11

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN pip install flask

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]