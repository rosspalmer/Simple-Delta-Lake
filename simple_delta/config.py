
from dataclasses import dataclass, asdict
import json
from typing import Dict, List


@dataclass
class SimpleDeltaConfig:
    name: str
    simple_home: str
    profile_path: str
    package_versions: Dict[str, str]
    warehouse_path: str = ""
    master_host: str = "localhost"
    worker_hosts: List[str] = list

    def get_version(self, package_name: str) -> str:
        return self.package_versions[package_name]

    def write(self, json_path: str):
        config_dict = asdict(self)
        with open(json_path, 'w') as write_file:
            json.dump(config_dict, write_file)


def read_config(json_path: str) -> SimpleDeltaConfig:
    with open(json_path, 'r') as read_file:
        config_dict = json.load(read_file)
        return SimpleDeltaConfig(**config_dict)
