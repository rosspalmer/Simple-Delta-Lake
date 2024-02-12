#!/bin/bash
set -e

# OpenJDK (Java) version for build
JAVA_VERSION="11.0.21+9"
# Install location of Java developer kit
JAVA_HOME="/usr/local/java"

# Construct download URL to specific OpenJDK (Java) binary
PACKAGE_NAME="OpenJDK11U-jdk_x64_linux_hotspot_${JAVA_VERSION/+/_}.tar.gz"
OPENJDK_BINARY="https://github.com/adoptium/temurin11-binaries/releases/download/jdk-${JAVA_VERSION/+/%2B}/$PACKAGE_NAME"

# Use `wget` to download OpenJDK (Java) binary archive in current directory
wget "$OPENJDK_BINARY"

tar -xvf "$PACKAGE_NAME"
mv "jdk-$JAVA_VERSION" "$JAVA_HOME"
rm "$PACKAGE_NAME"

# Add required environment variables to bash profile file
/usr/bin/cat <<EOF >> "$BASH_PROFILE"
export JAVA_HOME=$JAVA_HOME
export PATH=\$PATH:\$JAVA_HOME/bin
EOF
