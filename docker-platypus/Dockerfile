######################################################################################
# Dockerfile to install platypus alignment/indel caller.
######################################################################################
# Version:          0.1.0
# Software:         Platypus
# Software Version: latest
# Base Image:       molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/molubuntu:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Download and install htslib from samtools
RUN wget https://github.com/samtools/htslib/archive/1.2.1.tar.gz
RUN tar -xzvf 1.2.1.tar.gz
RUN rm -rf 1.2.1.tar.gz
WORKDIR $HOME/htslib-1.2.1
RUN make
RUN sudo make install

# Download and unzip Platypus
WORKDIR $HOME
RUN wget http://www.well.ox.ac.uk/bioinformatics/Software/Platypus-latest.tgz
RUN tar -xzvf Platypus-latest.tgz
RUN rm -rf Platypus-latest.tgz
RUN mv P* platypus

WORKDIR $HOME/platypus
RUN ./buildPlatypus.sh