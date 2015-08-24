######################################################################################
# Dockerfile to install platypus alignment/indel caller. Based on centos image.
######################################################################################

FROM molecular/molubuntu

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