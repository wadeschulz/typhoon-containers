FROM ubuntu:16.04

RUN apt-get -yy update && apt-get -yy upgrade
RUN apt-get -yy install python3 python3-pip
RUN apt-get -yy install build-essential python3-dev
RUN apt-get -yy install python3-scipy python3-numpy
RUN yes | pip3 install scikit-learn
RUN yes | pip3 install jupyter

RUN mkdir /home/jupyter

EXPOSE 8888
CMD jupyter notebook --ip='*' --no-browser --notebook-dir=/home/jupyter