######################################################################################
# Dockerfile to install cgHub download tools
######################################################################################
# Version:          0.2.0
# Software:         cghub
# Software Version: 3.8.7
# Base Image:       CentOS6
######################################################################################

FROM centos:centos6

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Download and install prereqs and cghub
RUN yum -y install wget libxerces-c-devel
RUN yum -y update
RUN wget https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.7/GeneTorrent-common-3.8.7-11.207.el6.x86_64.rpm
RUN wget https://cghub.ucsc.edu/software/downloads/GeneTorrent/3.8.7/GeneTorrent-download-3.8.7-11.207.el6.x86_64.rpm

RUN rpm -ivh GeneTorrent-common-3.8.7-11.207.el6.x86_64.rpm
RUN rpm -ivh GeneTorrent-download-3.8.7-11.207.el6.x86_64.rpm

RUN rm -f GeneTorrent-common-3.8.7-11.207.el6.x86_64.rpm GeneTorrent-download-3.8.7-11.207.el6.x86_64.rpm
RUN mkdir /home/cgHub
WORKDIR /home/cgHub