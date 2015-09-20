# Ghost.py
#
# VERSION 0.2
FROM centos:7
MAINTAINER  Arkii sqy6@163.com

WORKDIR /srv/app

RUN set -x \
        && echo 'Asia/Shanghai' > /etc/timezone \
        && /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
        && mkdir ~/.pip

COPY ./pip.conf ~/.pip/pip.conf
COPY ./CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo
COPY ./epel.repo /etc/yum.repos.d/epel.repo
COPY ./run.sh /run.sh

RUN set -x \
        && yum -y install python-setuptools python-pip PyQt4 PyQt4-webkit xorg-x11-server-Xvfb \
        && pip install ghost.py --pre \
        && pip install Flask \
        && pip install beautifulsoup4 \
        && rm -rf /var/lib/yum/*
CMD /run.sh
EXPOSE 80 5000 8000 8080
