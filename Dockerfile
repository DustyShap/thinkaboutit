FROM python:3.6.5
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code

ENV FLASK_ENV=development
ENV FLASK_APP=thinkaboutit/app.py
