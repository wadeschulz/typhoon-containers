######################################################################################
# Dockerfile to install Control-FREEC software
######################################################################################
# Version:          0.1.0
# Software:         Control-FREEC
# Software Version: 
# Base Image:       ubuntu:14.04
######################################################################################

FROM ubuntu:14.04

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Update apt-get and install packages
RUN apt-get -qq update
RUN apt-get -qqy install \
	build-essential \
	wget

# Create bio user and disable password requirement for sudo group
RUN useradd -r -m -U -d /home/bio -s /bin/bash -c "Bio User" -p '' bio
RUN usermod -a -G sudo bio
RUN sed -i "s/^\%sudo\tALL=(ALL:ALL)\sALL/%sudo ALL=(ALL) NOPASSWD:ALL/" /etc/sudoers
USER bio
ENV HOME /home/bio
WORKDIR $HOME

# Download and install bowtie2
RUN mkdir freec
WORKDIR $HOME/freec

RUN wget http://bioinfo-out.curie.fr/projects/freec/src/FREEC_Linux64.tar.gz
RUN tar -xzvf FREEC_Linux64.tar.gz && rm FREEC_Linux64.tar.gz
RUN make

ENV PATH $HOME/freec:$PATH
WORKDIR $HOME