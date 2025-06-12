#!/bin/bash

# Update package list and install build essentials for compiling C++ libs
apt-get update
apt-get install -y build-essential cmake python3-dev