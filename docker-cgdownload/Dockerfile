######################################################################################
# Dockerfile to install cgHub download tools and add script to directly download
# through docker run
######################################################################################
# Version:          0.4.0
# Software:         cghub
# Software Version: 3.8.7
# Base Image:       molecular/cghub<-CentOS6
######################################################################################

FROM molecular/cghub:latest

MAINTAINER Wade Schulz <wade.schulz@gmail.com>

COPY cgdownload.py cgdownload.py
ENTRYPOINT ["python", "cgdownload.py"]