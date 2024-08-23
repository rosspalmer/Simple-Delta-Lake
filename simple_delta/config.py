
from dataclasses import dataclass, asdict
import json
from typing import Dict, List


@dataclass
class ResourceConfig:
    host: str
    instances: int = 1


@dataclass
class SimpleDeltaConfig:
    name: str
    simple_home: str
    profile_path: str
    packages: Dict[str, str]
    warehouse_path: str = None
    master: ResourceConfig = ResourceConfig("localhost")
    master_cores: int = None
    master_memory: str = None
    workers: List[ResourceConfig] = list
    worker_cores: int = None
    worker_memory: str = None

    def get_package_version(self, package_name: str) -> str:
        return self.packages[package_name]

    def write(self, json_path: str):

        config_dict = asdict(self)
        if self.master:
            config_dict['master'] = asdict(config_dict['master'])
        if self.workers:
            config_dict['workers'] = list(map(lambda x: asdict(x), config_dict['workers']))

        with open(json_path, 'w') as write_file:
            json.dump(config_dict, write_file)


def read_config(json_path: str) -> SimpleDeltaConfig:

    with open(json_path, 'r') as read_file:

        config_dict = json.load(read_file)
        if 'master' in config_dict:
            config_dict['master'] = ResourceConfig(**config_dict['master'])
        if 'workers' in config_dict:
            config_dict['workers'] = list(map(lambda x: ResourceConfig(**x), config_dict))

        return SimpleDeltaConfig(**config_dict)
