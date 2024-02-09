#!/bin/bash
set -e

# Scala version for build
SCALA_VERSION="2.12.18"
# Install location of Scala developer kit
SCALA_HOME="/usr/local/scala"

# Construct download URL for specific Scala binary
SCALA_BINARY="https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz"

# Use `wget` to download Scala binary archive in current directory
wget "$SCALA_BINARY"

# Extract Scala binary, move to SCALA_HOME, and remove archive
tar -xvf scala-2.12.18.tgz
mv "scala-$SCALA_VERSION" "$SCALA_HOME"
rm scala-2.12.18.tgz

# Add required environment variables to bash profile file
/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export SCALA_HOME=$SCALA_HOME
export PATH=\$PATH:\$SCALA_HOME/bin
EOF