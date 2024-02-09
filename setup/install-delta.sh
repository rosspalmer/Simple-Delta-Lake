#!/bin/bash
set -e

# Delta-Spark (Delta.io) version for build
DELTA_VERSION="3.1.0"

source "$BASH_PROFILE"

/usr/bin/cat <<EOF >> "$SPARK_CONFIG"
spark.jars.packages io.delta:delta-spark_2.12:$DELTA_VERSION
spark.sql.extensions io.delta.sql.DeltaSparkSessionExtension
spark.sql.catalog.spark_catalog org.apache.spark.sql.delta.catalog.DeltaCatalog
EOF