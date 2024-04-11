# Use Ubuntu latest as the base image.
FROM ubuntu:24.04

# Dockblock.
LABEL maintainer="waan<admin@waan.email>"
LABEL description="Ubuntu Dev Container"
LABEL website="https://waan.io"
LABEL origin="https://github.com/waanlabs/code-challenges"
LABEL version="1.0.0"
LABEL license="MIT"

# Custom settings.
<<<<<<< HEAD
ARG USER=waan
=======
ARG USER=wired
>>>>>>> main
ARG UID=5000
ARG GID=5000
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

# Install common tools.
RUN apt-get update && \
    apt-get install -y software-properties-common \
    build-essential \
    git \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages.
RUN apt-get update && \
    apt-get install -y python3-pip \
    python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user, add to sudo group, and configure sudoers.
# Using useradd with explicit user/group IDs for consistency.
RUN groupadd -g ${GID} ${USER} && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER}

# Switch to new sudo user.
USER ${USER}

# Set the working directory.
WORKDIR /home/${USER}/${PROJECT}

# Set project folder permissions to current user.
RUN chown -R ${USER}:${USER} /home/${USER}/${PROJECT}

# Define the default entry point.
ENTRYPOINT ["/bin/bash"]
