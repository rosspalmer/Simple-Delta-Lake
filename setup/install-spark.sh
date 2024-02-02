#!/bin/bash
set -e

SPARK_VERSION="3.5.0"
SPARK_HOME="/usr/local/spark"

# Bash profile file (.bashrc, etc) where environment variables are set
BASH_PROFILE=$1

wget "https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz"
tar xvf "spark-$SPARK_VERSION-bin-hadoop3.tgz"
mv "spark-$SPARK_VERSION-bin-hadoop3" $SPARK_HOME

echo "export SPARK_HOME=$SPARK_HOME" >> "$BASH_PROFILE"
echo "export PATH=\$PATH:\$SPARK_HOME/bin" >> "$BASH_PROFILE"
