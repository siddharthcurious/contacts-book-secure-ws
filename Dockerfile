FROM python:2.7.15-slim-jessie
MAINTAINER Sadhyalal Kumar <sandhyalalkumar@gmail.com>

COPY ./ /app
WORKDIR /app

RUN apt-get update
RUN apt-get install sshpass -y
RUN pip install -r requirements.txt
RUN echo "    StrictHostKeyChecking no" >> /etc/ssh/ssh_config

ENV SERVICEHOST="0.0.0.0"
ENV SERVICEPORT=5000
ENV ENVIRONMENT="local"
ENV CONFIGSOURCE="file"

EXPOSE 5000

ENTRYPOINT python index.py
