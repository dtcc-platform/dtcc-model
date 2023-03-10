# This is the base Dockerfile for DTCC Platform. This file is part
# of the dtcc-model repository (which resides as a submodule in all
# other repositories). Docker images for all other repositories are
# built on top of this base image by adding specific dependencies
# via the install_dependencies.sh script.

# Use Phusion base image (minimal Docker-friendly Ubuntu)
FROM phusion/baseimage:master as base

# Set some variables
ENV USER dtcc
ENV HOME /home/$USER

# Install libraries used by other repos
COPY docker/install_scripts/ /
#COPY docker/createbanner.sh /

RUN apt-get update && apt-get install -y locales  sudo 

RUN ./install_dependencies.sh

# Add /usr/local/lib into LD
RUN ldconfig /usr/local/lib

# Add user and change to user
RUN useradd -m $USER -G sudo && \
    echo "$USER:$USER" | chpasswd && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN usermod -u 1001 dtcc
RUN groupmod -g 1001 dtcc

#RUN touch banner
#RUN ./createbanner.sh
#USER $USER

# Generate welcome message printed at login
#RUN touch banner
#RUN ./createbanner.sh
#COPY banner /
#COPY banner $HOME/.welcome
#COPY *docker/Welcome $HOME/.welcome
#RUN echo "cat $HOME/.welcome" >> $HOME/.bashrc

RUN mkdir /shared_data
RUN chown $USER:$USER /shared_data

# Image setup
FROM base as dev
USER $USER
ENTRYPOINT ["/bin/bash", "-l", "-c"]
CMD ["/bin/bash", "-i"]
