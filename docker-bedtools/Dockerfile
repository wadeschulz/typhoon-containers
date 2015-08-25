######################################################################################
# Dockerfile to install bedtools
######################################################################################
# Version:          0.1.0
# Software:         bedtools
# Software Version: latest
# Base Image:       ubuntu:14.04
######################################################################################

FROM ubuntu:14.04

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Install apt-get package dependencies
RUN apt-get -qq update
RUN apt-get -qqy install \
		bedtools

# Create bio user and disable password requirement for sudo group
RUN useradd -r -m -U -d /home/bio -s /bin/bash -c "Bio User" -p '' bio
RUN usermod -a -G sudo bio
RUN sed -i "s/^\%sudo\tALL=(ALL:ALL)\sALL/%sudo ALL=(ALL) NOPASSWD:ALL/" /etc/sudoers
USER bio
ENV HOME /home/bio
WORKDIR $HOME