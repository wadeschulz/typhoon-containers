######################################################################################
# Dockerfile to install bedtools
######################################################################################
# Version:          0.1.0
# Software:         bedtools
# Software Version: latest
# Base Image:       molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/molubuntu:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

RUN sudo apt-get -qqy install \
		libncurses-dev

ADD https://github.com/samtools/samtools/releases/download/1.2/samtools-1.2.tar.bz2 samtools-1.2.tar.bz2
RUN sudo tar -xjvf samtools-1.2.tar.bz2 && rm -rf samtools-1.2.tar.bz2
WORKDIR $HOME/samtools-1.2
RUN sudo make && sudo make install
WORKDIR $HOME