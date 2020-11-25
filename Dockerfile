FROM ubuntu:20.04

ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND noninteractive

# Java Install
RUN apt update -y
RUN apt install openjdk-14-jdk -y

# Python Install
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update -y
RUN apt install python3.8 -y
RUN apt install python3-pip -y

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip3 install -r requirements.txt
