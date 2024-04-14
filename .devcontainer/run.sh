#!/bin/bash

gpgconf --kill gpg-agent && gpg-agent --daemon
