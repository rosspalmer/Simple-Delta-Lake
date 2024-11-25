
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
    master: ResourceConfig
    derby_path: str = None
    warehouse_path: str = None
    metastore_config: HiveMetastoreConfig = None
    workers: List[ResourceConfig] = list
    executor_memory: str = None
    jdbc_drivers: dict[str, MavenJar] = None

    def __str__(self):

        config_dict = asdict(self)
        if self.master:
            config_dict['master'] = asdict(config_dict['master'])
        if self.workers:
            config_dict['workers'] = list(map(lambda x: asdict(x), config_dict['workers']))
        if self.metastore_config:
            config_dict['metastore_config'] = asdict(config_dict['metastore_config'])

        return json.dumps(config_dict)

    def get_package_version(self, package_name: str) -> str:
        return self.packages[package_name]

    def generate_template_json(self) -> str:
        template = SimpleDeltaConfig(
            name='<SETUP-NAME>',
            simple_home='<SIMPLE-SPARK-DIR>',
            profile_path='<PATH-TO-PROFILE-FILE>',
            packages={
                'java': '<OPENJDK-JAVA-VERSION>',
                'scala': '<SPARK-COMPATIBLE-SCALA-VERSION>',
                'spark': '<SPARK-VERSION>',
                'delta': '<OPTIONAL-DELTA-VERSION>',
                'hadoop': '<OPTIONAL-HADOOP-VERSION>',
                'hive': '<OPTIONAL-HIVE-VERSION>'
            },
            master=ResourceConfig(
                host='<MASTER-IP-ADDRESS>',
                cores=4,
                memory='4G'
            ),
            derby_path='<OPTIONAL-PATH-TO-LOCAL-DERBY-CATALOG>',
            warehouse_path='<OPTIONAL-PATH-TO-LOCAL-WAREHOUSE>',
            metastore_config=HiveMetastoreConfig(
                db_type='<mysql/postgres/oracle>',
                db_host='<DATABASE-IP-ADDRESS>',
                db_port=0,
                db_user='<DATABASE-LOGIN-USERNAME>',
                db_pass='<DATABASE-LOGIN-PASSWORD>'
            ),
            workers=[
                ResourceConfig(
                    host='<WORKER-IP-ADDRESS>',
                    cores=4,
                    memory='8G',
                    instances=8
                )
            ],
            executor_memory='8G',
            jdbc_drivers={
                'mysql': MavenJar('TODO', 'TODO', 'TODO'),
            }

        )

        return str(template)

    def write(self, json_path: str):

        as_string = str(self)

        with open(json_path, 'w') as write_file:
            write_file.write(as_string)


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
