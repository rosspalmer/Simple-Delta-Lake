#!/bin/bash
set -e

# Spark version for build
SPARK_VERSION="3.5.1"
# Install location of Spark package
SPARK_HOME="/usr/local/spark"

# Identify Spark config file location (will not exist initially)
SPARK_CONFIG="$SPARK_HOME/conf/spark-defaults.conf"

# Construct download URL for specific Spark binary
BINARY_FILE="spark-$SPARK_VERSION-bin-hadoop3"
SPARK_BINARY="https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/$BINARY_FILE.tgz"

# Download Spark binary archive into current directory
wget "$SPARK_BINARY"

# Extract Spark binary, move to SPARK_HOME, and remove archive
tar xf "$BINARY_FILE.tgz"
mv "$BINARY_FILE" "$SPARK_HOME"
rm "$BINARY_FILE.tgz"

# Add required environment variables to bash profile file
/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export SPARK_HOME=$SPARK_HOME
export SPARK_CONFIG=$SPARK_CONFIG
export PATH=\$PATH:\$SPARK_HOME/bin
EOF

# Create initial spark configuration file by copying over template
cp "$SPARK_CONFIG.template" "$SPARK_CONFIG"