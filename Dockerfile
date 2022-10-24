#Dockerfiles for running tensorflow entity

FROM python:3.8.5

RUN python -m pip --no-cache-dir install --upgrade pip
RUN pip install --upgrade pip

#Install Tensorflow
RUN python -m pip --no-cache-dir install tensorflow==2.10.0