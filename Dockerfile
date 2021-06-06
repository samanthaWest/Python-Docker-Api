FROM python:3.8-slim-buster

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip3 install --upgrade pip3

RUN pip3 install -r requirements.txt

EXPOSE 8080
CMD ["python3", "main.py"]