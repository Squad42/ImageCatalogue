FROM python:3.6.8-alpine

LABEL Squad42 project: image for ImageCatalogue microservice

COPY imageCatalogue/ /imageCatalogue
COPY requirements.txt /imageCatalogue/
WORKDIR /imageCatalogue/


RUN pip3 install --upgrade pip

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

RUN pip3 install -r requirements.txt

EXPOSE 5001

ENV FLASK_APP=server.py
CMD ["python3","-m","flask","run", "--host", "0.0.0.0", "--port", "5001"]
