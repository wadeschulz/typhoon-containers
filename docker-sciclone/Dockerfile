######################################################################################
# Dockerfile to install R and SciClone (https://github.com/genome/sciclone)
######################################################################################
# Version:          0.1.0
# Software:         R, SciClone
# Software Version: latest
# Base Image:       ubuntu:14.04
######################################################################################

FROM ubuntu:14.04

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Add CRAN R repository and key files for repository
RUN echo deb http://cran.rstudio.com/bin/linux/ubuntu trusty/ > /etc/apt/sources.list.d/rstudio.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9

# Update apt-get and install packages
RUN apt-get -qq update

RUN apt-get -qqy build-dep r-cran-rgl
RUN apt-get -qqy install \
		git \
		libcurl4-openssl-dev \
		libicu-dev \
		libxml2-dev \
		python-dev \
		python-pip \
		r-base \
		r-base-dev \
		r-cran-rgl

RUN pip install rpy2

# Create bio user and disable password requirement for sudo group
RUN useradd -r -m -U -d /home/bio -s /bin/bash -c "Bio User" -p '' bio
RUN usermod -a -G sudo bio
RUN sed -i "s/^\%sudo\tALL=(ALL:ALL)\sALL/%sudo ALL=(ALL) NOPASSWD:ALL/" /etc/sudoers
USER bio
ENV HOME /home/bio
WORKDIR $HOME

COPY sciclone-install.R sciclone-install.R
RUN sudo Rscript sciclone-install.R

ENV DEBIAN_FRONTEND interactive