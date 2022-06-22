# This file builds the Docker image for the Digital Twin Cities Platform

# Use Phusion base image (minimal Docker-friendly Ubuntu)
FROM phusion/baseimage:master as base

# Set some variables
ENV USER dtcc
ENV HOME /home/$USER
ENV DIR core

COPY docker/install_scripts/ /
# Avoid stall during installation of tzdata
#ENV TZ=Europe/Stockholm
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install libraries used by DTCCore
RUN ./install_dependencies.sh

# Add /usr/local/lib into LD
RUN ldconfig /usr/local/lib

# Add /usr/local/lib into LD
RUN ldconfig /usr/local/lib

# Add user and change to user
RUN useradd -m $USER -G sudo && \
    echo "$USER:$USER" | chpasswd && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER $USER

# Create shared volume
VOLUME $HOME/$DIR
WORKDIR $HOME/$DIR

# Generate welcome message printed at login
COPY dtcc-model/docker/Welcome $HOME/.welcome
RUN echo "cat $HOME/.welcome" >> $HOME/.bashrc

# Start bash login shell
#ENTRYPOINT ["/bin/bash", "-l", "-c"]
#CMD ["/bin/bash", "-i"]

FROM base as dev
USER $USER
ENTRYPOINT ["/bin/bash", "-l", "-c"]
CMD ["/bin/bash", "-i"]
