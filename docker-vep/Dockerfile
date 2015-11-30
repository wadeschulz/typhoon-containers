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

RUN sudo apt-get -qq update
RUN sudo apt-get -qqy install \
                curl \
                mysql-server \
                git \
                gzip \
                unzip

RUN curl -L http://cpanmin.us | sudo perl - App::cpanminus
RUN sudo cpanm Archive::Zip DBI

ADD https://github.com/Ensembl/ensembl-tools/archive/release/82.zip vep-82.zip
RUN sudo unzip vep-82.zip && rm -rf vep-82.zip
WORKDIR $HOME/ensembl-tools-release-82/scripts/variant_effect_predictor
RUN sudo perl INSTALL.pl --SPECIES homo_sapiens_refseq --ASSEMBLY GRCh37
ENV PATH $HOME/ensembl-tools-release-82/scripts/variant_effect_predictor:$PATH
WORKDIR $HOME