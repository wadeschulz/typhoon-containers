######################################################################################
# Dockerfile to install bamtools
######################################################################################
# Version:          0.1.0
# Software:         bamtools
# Software Version: 2.4.0
# Base Image:       molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/molubuntu:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Install apt-get package dependencies for CONIFER
RUN sudo apt-get -qqy install \
		cython \
		libhdf5-serial-dev \
		python-matplotlib \
		python-numpy \
		python-pip

ADD https://github.com/pezmaster31/bamtools/archive/v2.4.0.zip