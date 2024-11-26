from pathlib import Path
from pprint import pprint
from typing import Dict
from shutil import rmtree

from simple_delta.config import SimpleDeltaConfig
from simple_delta.setup import *


class SimpleEnvironment:

    def __init__(self, config: SimpleDeltaConfig, local_host: str):
        self.config = config
        self.local_host = local_host
        self.libs_path = f"{config.simple_home}/libs"

        self.package_urls: Dict[str, str] = {
            "java": "https://github.com/adoptium/temurin11-binaries/releases/download"
                    f"/jdk-{config.get_package_version('java').replace('+', '%2B')}",
            "scala": f"https://downloads.lightbend.com/scala/{config.get_package_version('scala')}",
            # FIXME use spark url which has older versions
            "spark": f"https://archive.apache.org/dist/spark/{config.get_package_version('spark')}",
        }

        self.package_names: Dict[str, str] = {
            "java": f"OpenJDK11U-jdk_x64_linux_hotspot_{config.get_package_version('java').replace('+', '_')}",
            "scala": f"scala-{config.get_package_version('scala')}",
            "spark": f"spark-{config.get_package_version('spark')}-bin-hadoop3"
        }

        self.package_extensions: Dict[str, str] = {
            "java": "tar.gz",
            "scala": "tgz",
            "spark": "tgz"
        }

    def archive_name(self, package: str) -> str:
        return f"{self.package_names[package]}.{self.package_extensions[package]}"

    def full_package_url(self, package: str) -> str:
        return f"{self.package_urls[package]}/{self.archive_name(package)}"

    def libs_directory(self) -> str:
        return f"{self.config.simple_home}/libs"

    def package_home_directory(self, package: str) -> str:
        return f"{self.libs_directory()}/{self.package_names[package]}"

    def spark_home(self) -> str:
        return self.package_home_directory("spark")

    def spark_jars_path(self) -> str:
        return f"{self.spark_home()}/jars"

    def spark_config_path(self) -> str:
        return f"{self.spark_home()}/conf/spark-defaults.conf"

    def spark_env_sh_path(self) -> str:
        return f"{self.spark_home()}/conf/spark-env.sh"

    def hive_config_path(self) -> str:
        return f"{self.spark_home()}/conf/hive-site.xml"

    def sync(self):

        print("Syncing environment:")
        pprint(self.config.__dict__)

        print(f"Simple-Delta HOME directory: {self.config.simple_home}")
        simple_home = Path(self.config.simple_home)
        if not simple_home.exists():
            simple_home.mkdir()
        rmtree(self.libs_path, ignore_errors=True)

        required_tasks: Dict[str, SetupTask] = {
            "install_java": SetupJavaBin("java", {
                "JAVA_HOME": f"{self.libs_path}/jdk-{self.config.get_package_version('java')}",
                "PATH": "$PATH:$JAVA_HOME/bin"}),
            "install_scala": SetupJavaBin("scala", {
                "SCALA_HOME": self.package_home_directory('scala'),
                "PATH": "$PATH:$SCALA_HOME/bin"}),
            "install_spark": SetupJavaBin("spark", {
                "SPARK_HOME": self.package_home_directory('spark'),
                "PATH": "$PATH:$SPARK_HOME/bin"}),
            "setup_master": SetupMasterConfig(),
            "setup_envs": SetupEnvsScript(),
        }

        optional_tasks: Dict[str, SetupTask] = {
            "setup_metastore": SetupHiveMetastore(),
            "install_delta": SetupDelta(),
        }

        include_optional_tasks: List[str] = []
        if self.config.metastore_config:
            include_optional_tasks.append("setup_metastore")
        if "delta" in self.config.packages:
            include_optional_tasks.append("install_delta")

        for task_name, task in required_tasks.items():
            task.run(self)

        for task_name in include_optional_tasks:
            task = optional_tasks[task_name]
            task.run(self)
