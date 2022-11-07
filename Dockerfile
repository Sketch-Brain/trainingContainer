#Dockerfiles for running tensorflow entity

FROM python:3.8.5
RUN mkdir /worker
WORKDIR /worker

COPY . .

RUN python -m pip --no-cache-dir install --upgrade pip
RUN pip install --upgrade pip

#Install Tensorflow
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]