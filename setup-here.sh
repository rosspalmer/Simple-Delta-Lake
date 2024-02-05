#!/bin/bash
set -e

apt install git -y

pushd /usr/local/src
git clone https://github.com/rosspalmer/Simple-Delta-Lake.git

pushd Simple-Delta-Lake/setup

bash install-java.sh
bash install-spark.sh
bash install-delta.sh