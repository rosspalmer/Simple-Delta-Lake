#!/bin/bash
set -e

BASH_PROFILE=$1
source "$BASH_PROFILE"

DELTA_VERSION="3.1.0"

/usr/bin/cat <<EOF >> "$SPARK_HOME"
spark.jars.packages io.delta:delta-spark_2.13:$DELTA_VERSION
spark.sql.extensions io.delta.sql.DeltaSparkSessionExtension
spark.sql.catalog.spark_catalog org.apache.spark.sql.delta.catalog.DeltaCatalog
EOF
