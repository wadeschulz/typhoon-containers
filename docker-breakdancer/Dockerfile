######################################################################################
# Dockerfile to install breakdancer alignment software
######################################################################################
# Version:          0.1.0
# Software:         breakdancer
# Software Version: 1.4.5
# Base Image:       samtools:0.1.0 <- molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/samtools:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Download and install prereqs
RUN sudo apt-get update
RUN sudo apt-get -qqy install \
		cmake \
		curl \
		libncurses5-dev \
		libncursesw5-dev \
		libgd-gd2-perl

# Install Perl dependencies
RUN curl -L http://cpanmin.us | sudo perl - App::cpanminus
RUN sudo cpanm \
		GD::Text \
		GD::Graph::histogram \
		Math::CDF \
		Statistics::Descriptive

# Download breakdancer
ADD https://github.com/genome/breakdancer/archive/v1.4.5.zip $HOME/breakdancer-1.4.5.zip
RUN sudo chown bio:bio breakdancer-1.4.5.zip
RUN unzip breakdancer-1.4.5.zip && rm -f breakdancer-1.4.5.zip

# Build breakdancer
WORKDIR $HOME/breakdancer-1.4.5
RUN mkdir build
WORKDIR $HOME/breakdancer-1.4.5/build
RUN cmake .. -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr/local
RUN make
RUN sudo make install

WORKDIR $HOME

ENV PATH $HOME/breakdancer-1.4.5/build/vendor/samtools/misc:$PATH
ENV PATH $HOME/breakdancer-1.4.5/perl:$PATH