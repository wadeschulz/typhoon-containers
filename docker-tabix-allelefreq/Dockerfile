######################################################################################
# Dockerfile to install tabix/vcftools and grab allele frequency from 1000 Genomes
# Data.
#    http://www.gettinggeneticsdone.com/2011/04/how-to-get-allele-frequencies-and.html
######################################################################################
# Version:          0.1.0
# Software:         Tabix, VCFtools
# Software Version: Tabix 0.2.6; VCFtools 0.1.13
# Base Image:       molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/molubuntu:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

# Download and install Tabix
RUN wget http://sourceforge.net/projects/samtools/files/tabix/tabix-0.2.6.tar.bz2
RUN tar -jxvf tabix-0.2.6.tar.bz2
RUN rm -rf tabix-0.2.6.tar.bz2
WORKDIR $HOME/tabix-0.2.6
RUN make

# Download and install VCFtools
WORKDIR $HOME
RUN wget https://github.com/vcftools/vcftools/archive/v0.1.13.tar.gz -O vcftools-0.1.13.tar.gz
RUN tar -zxvf vcftools-0.1.13.tar.gz
RUN rm -rf vcftools-0.1.13.tar.gz
WORKDIR $HOME/vcftools-0.1.13/
RUN make
RUN make install

WORKDIR $HOME

RUN mkdir calc_allele_freq
WORKDIR $HOME/calc_allele_freq/
COPY calc_allele_freq.py calc_allele_freq.py