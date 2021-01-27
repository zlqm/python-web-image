#!/bin/bash
set -e
source /bd_build/buildconfig

echo "Installing Python..."
minimal_apt_get_install(){
	apt-get install -y --no-install-recommends $1
}

apt-get update
## Install Python.
minimal_apt_get_install python3.8
minimal_apt_get_install python3-distutils
# minimal_apt_get_install python3.8-dev
curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
cd /tmp && python3.8 get-pip.py 
pip3 install setuptools
