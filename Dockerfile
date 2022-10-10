FROM python:3.9.13
LABEL author="Sergey"
LABEL email="korolev.s@ittest-team.ru"

ENV REFRESHED_AT=2022-09-07
ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get -yqq update && apt-get -yqq upgrade

RUN apt-get install -yqq python3 \
                         python3-pip \
                         software-properties-common \
                         wget \
                         unzip

RUN apt-get install chromium -y




ADD . ./
WORKDIR /tests

RUN pip3 install -r ../requerements.txt


CMD [  "pytest" ]