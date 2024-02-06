#!/bin/bash
set -e

# Bash profile file (.bashrc, etc) where environment variables are set
BASH_PROFILE=$1

SCALA_HOME=/usr/local/spark
SCALA_BINARY=https://downloads.lightbend.com/scala/2.12.18/scala-2.12.18.tgz

wget "$SCALA_BINARY"

mkdir "$SCALA_HOME"
tar -xvf scala-2.12.18.tgz -C "$SCALA_HOME"
rm scala-2.12.18.tgz

/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export SCALA_HOME=$SCALA_HOME/scala-2.12.18
export PATH=\$PATH:\$SCALA_HOME/bin
EOF