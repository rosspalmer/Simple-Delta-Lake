#!/bin/bash
set -e

# Hadoop (HDFS) version for build
HADOOP_VERSION="3.2.4"
# Install location of Hadoop package
HADOOP_HOME="/usr/local/hadoop"

# Construct download URL for Hadoop package based on version
HADOOP_BINARY="https://dlcdn.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"

# Download Spark binary archive into current directory
wget "$HADOOP_BINARY"

# Extract Spark binary, move to SPARK_HOME, and remove archive
tar -xf "hadoop-$HADOOP_VERSION.tar.gz"
mv "hadoop-$HADOOP_VERSION" "$SPARK_HOME"
rm "hadoop-$HADOOP_VERSION.tar.gz"

# Add required environment variables to bash profile file
/usr/bin/cat <<EOF >> "$BASH_PROFILE"
# Set Hadoop (HDFS) home location and add binaries to PATH
export HADOOP_HOME=$HADOOP_HOME
export PATH=\$PATH:\$HADOOP_HOME/bin:\$HADOOP_HOME/sbin

# Set homes for Hadoop components to same home folder
export HADOOP_INSTALL=\$HADOOP_HOME
export HADOOP_MAPRED_HOME=\$HADOOP_HOME
export HADOOP_COMMON_HOME=\$HADOOP_HOME
export HADOOP_HDFS_HOME=\$HADOOP_HOME

# TODO
export HADOOP_COMMON_LIB_NATIVE_DIR=\$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=\$HADOOP_COMMON_LIB_NATIVE_DIR"
EOF

