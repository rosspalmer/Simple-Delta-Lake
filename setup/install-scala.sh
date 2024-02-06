#!/bin/bash
set -e

# Bash profile file (.bashrc, etc) where environment variables are set
BASH_PROFILE=$1

SCALA_VERSION="2.12.18"

SCALA_HOME=/usr/local/scala
SCALA_BINARY="https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz"

wget "$SCALA_BINARY"

tar -xvf scala-2.12.18.tgz
mv "scala-$SCALA_VERSION" "$SCALA_HOME"
rm scala-2.12.18.tgz

/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export SCALA_HOME=$SCALA_HOME
export PATH=\$PATH:\$SCALA_HOME/bin
EOF