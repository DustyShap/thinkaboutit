FROM python:3.6.5
RUN pip install --upgrade pip
RUN mkdir /thinkaboutit
WORKDIR /thinkaboutit
ADD requirements.txt /thinkaboutit/
RUN pip install -r requirements.txt
ADD . /thinkaboutit

ENV FLASK_ENV=development
ENV FLASK_APP=thinkaboutit/app.py
