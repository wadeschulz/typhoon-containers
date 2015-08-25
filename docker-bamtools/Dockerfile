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

# Install apt-get package dependencies
RUN sudo apt-get -qqy install \
		cmake

# Download and extract bamtools binaries
ADD https://github.com/pezmaster31/bamtools/archive/v2.4.0.zip bamtools.zip
RUN sudo unzip bamtools.zip && rm -rf bamtools.zip
RUN sudo mkdir $HOME/bamtools-2.4.0/build
WORKDIR $HOME/bamtools-2.4.0/build
RUN sudo cmake ..
RUN sudo make
WORKDIR $HOME/bamtools-2.4.0/bin
ENTRYPOINT ["./bamtools-2.4.0"]