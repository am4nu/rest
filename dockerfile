FROM ubuntu:18.04
MAINTAINER  mo.amanuddin@gmail.com

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && apt-get install nano

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "bash" ]

#CMD [ "bash" ]