######################################################################################
# Dockerfile for Elasticsearch
######################################################################################
# Version:          0.1.0
# Software:         Elasticsearch
# Version:                      2.2.0
# Base Image:       CentOS7
######################################################################################

FROM centos:centos7

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Download and install epel release, update yum
RUN yum -y install epel-release
RUN yum -y update

RUN yum -y install java-1.8.0-openjdk.x86_64 \
        wget

RUN wget https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/rpm/elasticsearch/2.1.1/elasticsearch-2.1.1.rpm
RUN rpm -ivh elasticsearch-2.1.1.rpm
