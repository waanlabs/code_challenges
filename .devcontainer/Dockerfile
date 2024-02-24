# Use Ubuntu latest as the base image
FROM ubuntu:22.04

# Dockblock
LABEL maintainer="waan<admin@waan.email>"
LABEL description="Ubuntu 22.04 Dev Container"
LABEL website="https://waan.io"
LABEL upstream="https://github.com/waanlabs/code-challenges"
LABEL version="1.0.0"
LABEL license="MIT"

# Set non-interactive to avoid prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Set the timezone to EST (Eastern Standard Time)
ENV TZ=EST

# Update package lists and install sudo with minimal additional packages
# Clean up in the RUN statement to keep the image size down
RUN apt-get update \
    && apt-get install sudo

# Create a non-root user, add to sudo group, and configure sudoers
# Using useradd with explicit user/group IDs for consistency
ARG USER=waan
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} ${USER} && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER}

# Switch to new user in the docker image
USER ${USER}

# Set the working directory
WORKDIR /home/${USER}/code-challenges

RUN sudo apt-get install -y software-properties-common \
    git \
    python3-pip \
    python3-venv \
    && sudo apt-get clean \
    && sudo rm -rf /var/lib/apt/lists/*

# Define the default command or entry point
CMD ["/bin/bash"]
