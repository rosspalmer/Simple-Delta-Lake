
from dataclasses import dataclass


@dataclass
class SimpleDeltaConfig:
    name: str
    simple_home: str
    profile_path: str
    java_version: str = "11.0.21+9"
    hadoop_version: str = "3.2.4"
    scala_version: str = "2.12.18"
    spark_version: str = "3.5.2"
    delta_version: str = "3.2.0"
