######################################################################################
# Dockerfile to install Bowtie2 alignment software
######################################################################################
# Version:          0.1.0
# Software:         bowtie2
# Software Version: 2.2.5
# Base Image:       molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/molubuntu:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Download and install bowtie2
RUN wget http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.5/bowtie2-2.2.5-linux-x86_64.zip
RUN unzip bowtie2-2.2.5-linux-x86_64.zip
RUN rm -rf bowtie2-2.2.5-linux-x86_64.zip

ENV PATH $HOME/bowtie2-2.2.5:$PATH
ENV BT2_HOME $HOME/bowtie2-2.2.5