#!/bin/bash
set -e

BASH_PROFILE=$1

pushd setup

bash install-java.sh "$BASH_PROFILE"
bash install-spark.sh "$BASH_PROFILE"
bash install-delta.sh "$BASH_PROFILE"
