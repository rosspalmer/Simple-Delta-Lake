#!/bin/bash
set -e

BASH_PROFILE=$1

bash install-java.sh
bash install-spark.sh "$BASH_PROFILE"
