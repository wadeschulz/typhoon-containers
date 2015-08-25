######################################################################################
# Dockerfile to install Confifer CNV analysis software
######################################################################################
# Version:          0.1.0
# Software:         CoNIFER
# Software Version: 0.2.2
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

# Install pip package dependencies for CONIFER
RUN sudo pip install \
		pysam \
		tables

RUN wget http://sourceforge.net/projects/conifer/files/CoNIFER%200.2.2/conifer_v0.2.2.tar.gz
RUN tar -xzvf conifer_v0.2.2.tar.gz
RUN rm -rf conifer_v0.2.2.tar.gz
ENV PATH $HOME/conifer_v0.2.2:$PATH

# Requires tables v3.1.1 to avoid HDF5 illegal instruction exception
RUN sudo pip uninstall -y tables
RUN sudo pip install tables==3.1.1