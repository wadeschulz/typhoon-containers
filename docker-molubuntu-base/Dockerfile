######################################################################################
# Base Ubuntu image for several NGS bioinformatics tools
######################################################################################
# Version:          0.1.0
# Software:         Ubuntu with build-essential, g++, python/dev, unzip, wget, zlib1g
# Software Version: 14.04
# Base Image:       ubuntu:14.04
######################################################################################

FROM ubuntu:14.04

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Update apt-get and install packages
RUN apt-get -qq update
RUN apt-get -qqy install \
		build-essential \
 		g++ \
		python \
		python-dev \
		unzip \
		wget \
		zlib1g-dev

# Create bio user and disable password requirement for sudo group
RUN useradd -r -m -U -d /home/bio -s /bin/bash -c "Bio User" -p '' bio
RUN usermod -a -G sudo bio
RUN sed -i "s/^\%sudo\tALL=(ALL:ALL)\sALL/%sudo ALL=(ALL) NOPASSWD:ALL/" /etc/sudoers
USER bio
ENV HOME /home/bio
WORKDIR $HOME
