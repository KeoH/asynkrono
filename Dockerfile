FROM python:3.6-slim-stretch

 ENV PYTHONUNBUFFERED 1

 RUN mkdir /code

 WORKDIR /code

 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 
 ADD . /code/