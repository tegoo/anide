FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

RUN yes | unminimize
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install man apt-utils bash-completion

RUN apt-get -y install \
        apt-utils \
        tzdata \
        ca-certificates curl \
        locales \
        less tmux python3 \
        git

RUN sed -i '/en_US.UTF-8/s/^# //' /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

RUN useradd -m developer --shell /bin/bash
USER developer
WORKDIR /home/developer

ENV APPIMAGE_EXTRACT_AND_RUN=1

ARG NVIM_URL="https://github.com/neovim/neovim/releases/download/v0.6.1/nvim.appimage"
ARG NVIM_SUM="ef9056e05ef6a4c1d0cdb8b21f79261703122c0fd31f23f782158d326fdadbf5  nvim"
RUN mkdir -p ~/downloads && cd ~/downloads && \
    echo "$NVIM_SUM" > nvim.sha256sum && \
    curl -L -o nvim "$NVIM_URL" && \
    sha256sum -c nvim.sha256sum && \
    mkdir -p ~/bin && cp nvim ~/bin/ && \
    chmod u+x ~/bin/nvim

ARG PLUG_URL="https://raw.githubusercontent.com/junegunn/vim-plug/0.11.0/plug.vim"
ARG PLUG_SUM="0d4dc422c3151ff651063b251933b3465714c5b9f3226faf0ca7f8b4a440a552  plug.vim"
RUN mkdir -p ~/downloads && cd ~/downloads && \
    echo "$PLUG_SUM" > plug.vim.sha256sum && \
    curl -L -o plug.vim "$PLUG_URL" && \
    sha256sum -c plug.vim.sha256sum && \
    mkdir -p ~/.local/share/nvim/site/autoload && \
    cp plug.vim ~/.local/share/nvim/site/autoload/

COPY entrypoint.py /home/developer/
ENTRYPOINT ["/usr/bin/python3", "/home/developer/entrypoint.py"]

COPY --chown=developer:developer config/nvim/init.lua /home/developer/.config/nvim/init.lua
COPY --chown=developer:developer config/tmux.conf /home/developer/.tmux.conf

ENV TERM=tmux-256color

