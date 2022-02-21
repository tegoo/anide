FROM ubuntu:20.04

RUN yes | unminimize
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install man apt-utils bash-completion

RUN apt-get -y install \
        less tmux python3

RUN useradd -m developer --shell /bin/bash
USER developer

COPY entrypoint.py /home/developer/
ENTRYPOINT ["/usr/bin/python3", "/home/developer/entrypoint.py"]

