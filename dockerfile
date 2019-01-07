FROM ubuntu:18.04
LABEL maintainer="mo amanuddin <mo.amanuddin@gmail.com>"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && apt-get install nano

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN pip3 install --user flask sqlalchemy flask-sqlalchemy

COPY . /app

RUN python3 setup.py

ENTRYPOINT [ "python3", "app.py" ]

#CMD [ "bash" ]