#!/bin/bash
set -e

# Bash profile file (.bashrc, etc) where environment variables are set
BASH_PROFILE=$1

SPARK_VERSION="3.5.0"
SPARK_HOME="/usr/local/spark"
SPARK_CONFIG="$SPARK_HOME/conf/spark-defaults.conf"
SPARK_BINARY="spark-$SPARK_VERSION-bin-hadoop3"

wget "https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz"
tar xvf "$SPARK_BINARY.tgz"
mv "$SPARK_BINARY" "$SPARK_HOME"
rm "$SPARK_BINARY.tgz"

/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export SPARK_HOME=$SPARK_HOME
export SPARK_CONFIG=$SPARK_CONFIG
export PATH=\$PATH:\$SPARK_HOME/bin
EOF

cp "$SPARK_CONFIG.template" "$SPARK_CONFIG"