#!/bin/bash

# sed -i 's/\r$//' run.sh - to remove carriage return.
# Start a new GPG agent.
gpgconf --kill gpg-agent && gpg-agent --daemon
