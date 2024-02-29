#!/bin/bash
set -e

BASH_PROFILE=$1

if [[ -z "$BASH_PROFILE" ]]
then
  echo "FAIL: Need to define BASH_PROFILE as first argument"
  exit 1
fi

export BASH_PROFILE=$BASH_PROFILE

pushd install

# Install Java and Scala SDKs
bash install-java.sh
bash install-scala.sh

# Install Spark with Hadoop + Hive metastore
bash install-spark.sh
bash install-hadoop.sh
bash install-hive.sh

# Install Delta library
bash install-delta.sh
