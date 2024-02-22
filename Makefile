
all: hadoop delta
	bash -c "echo Done!"

java:
	bash -c "pushd make; bash install-java.sh; popd"

scala: java
	bash -c "pushd make; bash install-scala.sh; popd"

spark: scala
	bash -c "pushd make; bash install-spark.sh; popd"

delta: spark
	bash -c "pushd make; bash install-delta.sh; popd"

hadoop: spark
	bash -c "pushd make; bash install-hadoop.sh; popd"

