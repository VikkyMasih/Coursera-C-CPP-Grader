FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get install -y python3 build-essential zip unzip

RUN mkdir -p /grader/

COPY files/ /grader/

RUN chmod a+rwx -R /grader/

ENTRYPOINT ["grader/grader.py"]