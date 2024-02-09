#!/bin/bash
set -e

BASH_PROFILE=$1

if [[ -z "$BASH_PROFILE" ]]
then
  echo "FAIL: Need to pass BASH_PROFILE as first argument"
  exit 1
fi

export BASH_PROFILE=$BASH_PROFILE

pushd setup

bash install-java.sh
bash install-scala.sh
bash install-spark.sh
bash install-delta.sh
