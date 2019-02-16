FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update \
    && apt-get -y install libmysqlclient-dev \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# FROM mysql:5.7
# USER mysql
# COPY ./setconf.sh .
# COPY config/my.cnf /etc/mysql/conf.d
# CMD [ "./setconf.sh" ]