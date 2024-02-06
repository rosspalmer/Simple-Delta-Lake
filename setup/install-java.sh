#!/bin/bash
set -e

# Bash profile file (.bashrc, etc) where environment variables are set
BASH_PROFILE=$1

JAVA_HOME=/usr/local/java
OPENJDK_BINARY="https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.21%2B9/OpenJDK11U-jdk_x64_linux_hotspot_11.0.21_9.tar.gz"

wget "$OPENJDK_BINARY"

tar -xvf OpenJDK11*.tar.gz
mv "jdk-11.0.21+9" $JAVA_HOME
rm OpenJDK11*.tar.gz

/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export JAVA_HOME=$JAVA_HOME
export PATH=\$PATH:\$JAVA_HOME/bin
EOF
