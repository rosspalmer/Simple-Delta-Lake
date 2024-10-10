
from dataclasses import dataclass, asdict
import json
from typing import Dict, List


@dataclass
class ResourceConfig:
    host: str
    cores: int = None
    memory: str = None
    instances: int = None


@dataclass
class HiveMetastoreConfig:
    db_type: str
    db_host: str
    db_port: int
    db_user: str
    db_pass: str


@dataclass
class MavenJar:
    group_id: str
    artifact_id: str
    version: str
    main_class: str = None


@dataclass
class SimpleDeltaConfig:
    name: str
    simple_home: str
    profile_path: str
    packages: Dict[str, str]
    derby_path: str = None
    warehouse_path: str = None
    metastore_config: HiveMetastoreConfig = None
    master: ResourceConfig = None
    workers: List[ResourceConfig] = list
    executor_memory: str = None
    jdbc_drivers: dict[str, MavenJar] = None

    def get_package_version(self, package_name: str) -> str:
        return self.packages[package_name]

    def write(self, json_path: str):

        config_dict = asdict(self)
        if self.master:
            config_dict['master'] = asdict(config_dict['master'])
        if self.workers:
            config_dict['workers'] = list(map(lambda x: asdict(x), config_dict['workers']))
        if self.metastore_config:
            config_dict['metastore_config'] = asdict(config_dict['metastore_config'])

        with open(json_path, 'w') as write_file:
            json.dump(config_dict, write_file)


def read_config(*json_path: str) -> SimpleDeltaConfig:

    config_dict = {}

    for path in json_path:
        with open(path, 'r') as read_file:
            config_dict = config_dict | json.load(read_file)

    if 'master' in config_dict:
        config_dict['master'] = ResourceConfig(**config_dict['master'])
    if 'workers' in config_dict:
        config_dict['workers'] = list(map(lambda x: ResourceConfig(**x), config_dict['workers']))
    if 'metastore_config' in config_dict:
        config_dict['metastore_config'] = HiveMetastoreConfig(**config_dict['metastore_config'])

    return SimpleDeltaConfig(**config_dict)
