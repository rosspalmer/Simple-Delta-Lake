
from dataclasses import dataclass, asdict
import json


@dataclass
class SimpleDeltaConfig:
    name: str
    simple_home: str
    profile_path: str
    java_version: str
    hadoop_version: str
    scala_version: str
    spark_version: str
    delta_version: str

    def write(self, json_path: str):
        config_dict = asdict(self)
        with open(json_path, 'w') as write_file:
            json.dump(config_dict, write_file)


def read_config(json_path: str) -> SimpleDeltaConfig:
    with open(json_path, 'r') as read_file:
        config_dict = json.load(read_file)
        return SimpleDeltaConfig(**config_dict)

