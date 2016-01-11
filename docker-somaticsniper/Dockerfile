######################################################################################
# Dockerfile to install SomaticSniper
######################################################################################
# Version:          0.2.0
# Software:         somaticsniper
# Software Version: 1.5.0
# Base Image:       molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/molubuntu:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

RUN sudo apt-get -qqy update
RUN sudo apt-get -qqy install \
	cmake \
	git-core \
	libncurses-dev

RUN git clone git://github.com/genome/somatic-sniper.git
RUN mkdir somatic-sniper/build
WORKDIR somatic-sniper/build
RUN cmake ../ && make deps && make -j && make test
RUN sudo make install
WORKDIR $HOME
RUN rm -rf somatic-sniper