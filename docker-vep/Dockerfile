######################################################################################
# Dockerfile to install Ensembl VEP
######################################################################################
# Version:          0.1.0
# Software:         ensembl-vep
# Software Version: latest
# Base Image:       molubuntu:0.1.0 <- ubuntu:14.04
######################################################################################

FROM molecular/molubuntu:0.1.0

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

#RUN sudo apt-get -qqy install software-properties-common
#RUN sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"
RUN sudo apt-get -qq update
RUN sudo apt-get -qqy install \
				bgzip \
                curl \
                mysql-server \
                git \
                gzip \
                unzip \
                wget

# Download and install Tabix
ADD http://sourceforge.net/projects/samtools/files/tabix/tabix-0.2.6.tar.bz2 tabix-0.2.6.tar.bz2
RUN tar -jxvf tabix-0.2.6.tar.bz2
RUN rm -rf tabix-0.2.6.tar.bz2
WORKDIR $HOME/tabix-0.2.6
RUN make
ENV PATH $HOME/tabix-0.2.6:$PATH

# Install CURL and cpanminus
RUN curl -L http://cpanmin.us | sudo perl - App::cpanminus
RUN sudo cpanm Archive::Zip DBI

# Install Ensembl VEP scripts
ADD https://github.com/Ensembl/ensembl-tools/archive/release/82.zip vep-82.zip
RUN unzip vep-82.zip && rm -rf vep-82.zip
WORKDIR $HOME/ensembl-tools-release-82/scripts/variant_effect_predictor
RUN sudo perl INSTALL.pl --SPECIES homo_sapiens_refseq --ASSEMBLY GRCh37
