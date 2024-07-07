from dataclasses import dataclass


@dataclass
class SimpleEnvironment:
    name: str
    setup_path: str
    profile_path: str = "~/.bashrc"
    java_version: str = "11.0.21+9"
    scala_version: str = "2.12.18"
    spark_version: str = "3.5.1"
