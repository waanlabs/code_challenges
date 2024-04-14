# Use Ubuntu 24.04 as the base image.
FROM ubuntu:24.04

# Dockblock.
LABEL maintainer="waan<admin@waan.email>"
LABEL description="Ubuntu Dev Container"
LABEL website="https://waan.io"
LABEL origin="https://github.com/waanlabs/code_challenges"
LABEL version="1.0.0"
LABEL license="MIT"

# Custom settings.
ARG USER=wired
ARG PROJECT=code_challenges

# Set non-interactive to avoid prompts during build.
ENV DEBIAN_FRONTEND=noninteractive

# Set the timezone to EST (Eastern Standard Time).
ENV TZ=EST

# Update package lists and install sudo.
RUN apt-get update && \
    apt-get install -y sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install common tools and Python packages.
RUN apt-get update && \
    apt-get install -y software-properties-common \
    build-essential \
    git \
    curl \
    pinentry-tty \
    vim \
    python3-pip \
    python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install vim.
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install pinentry-tty for GPG.
RUN apt-get update && \
    apt-get install pinentry-tty -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user, add to sudo group, and configure sudoers.
RUN groupadd ${USER} && \
    useradd -m -s /bin/bash -g ${USER} ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER}

# Add TTY to .bashrc for GPG.
RUN echo 'export GPG_TTY=$(tty)' >> ~/.bashrc

# Switch to new sudo user.
USER ${USER}

# Set user and group ownership to current user.
RUN chown -R ${USER}:${USER} /home/${USER}/${PROJECT}

# Set the working directory.
WORKDIR /home/${USER}/${PROJECT}

# Set user and group ownership to current user.
RUN sudo chown -R ${USER}:${USER} /home/${USER}/${PROJECT}

# Define the default entry point.
ENTRYPOINT ["/bin/bash"]
