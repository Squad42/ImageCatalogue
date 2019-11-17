FROM python:3.6.8-alpine

LABEL Squad42 project: image for ImageCatalogue microservice

COPY imageCatalogue/ /imageCatalogue
COPY requirements.txt /imageCatalogue/
WORKDIR /imageCatalogue/


RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev 
RUN apk --no-cache add postgresql-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip3 install --upgrade pip
RUN pip3 install psycopg2
RUN pip3 install psycopg2-binary
RUN pip3 install -r requirements.txt

EXPOSE 5001

ENV FLASK_APP=server.py
CMD ["python3","-m","flask","run", "--host", "0.0.0.0", "--port", "5001"]
