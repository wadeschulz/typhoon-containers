######################################################################################
# Dockerfile for Luigi with cron
######################################################################################
# Version:          0.1.0
# Software:         python 2.7, luigi
# Base Image:       CentOS7
######################################################################################

FROM centos:centos7

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Download and install epel release, update yum
RUN yum -y install epel-release
RUN yum -y update

# install cron, python reqs for luigid
RUN yum -y install \
        cronie \
        python-daemon \
        python-pip \
        sqlite

# Create directories for luigid and modules
RUN mkdir /opt/luigi && mkdir /opt/luigi/logs && mkdir /opt/luigi/modules
ENV PYTHONPATH=$PYTHONPATH:/opt/luigi/modules

# Install sqlalchemy for luigid
RUN yes | pip install luigi sqlalchemy
COPY luigi.cfg /etc/luigi/client.cfg

WORKDIR /opt/luigi/modules

# Start cron, luigi and load bash
CMD /usr/sbin/crond & luigid --background --pidfile /opt/luigi/luigi.pid --logdir /opt/luigi/logs --state-path /opt/luigi/luigi-state.pickle & /bin/bash
