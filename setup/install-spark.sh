#!/bin/bash
set -e

# Spark version for build
SPARK_VERSION="3.5.0"
# Install location
SPARK_HOME="/usr/local/spark"

BINARY_FILE="spark-$SPARK_VERSION-bin-hadoop3"
SPARK_BINARY="https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/$BINARY_FILE.tgz"
SPARK_CONFIG="$SPARK_HOME/conf/spark-defaults.conf"

wget "$SPARK_BINARY"

tar xvf "$BINARY_FILE.tgz"
mv "$BINARY_FILE" "$SPARK_HOME"
rm "$BINARY_FILE.tgz"

# Add required environment variables to bash profile file
/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export SPARK_HOME=$SPARK_HOME
export SPARK_CONFIG=$SPARK_CONFIG
export PATH=\$PATH:\$SPARK_HOME/bin
EOF

cp "$SPARK_CONFIG.template" "$SPARK_CONFIG"