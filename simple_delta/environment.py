
from typing import Dict

from simple_delta.config import SimpleDeltaConfig


class SimpleEnvironment:

    def __init__(self, config: SimpleDeltaConfig, local_host: str):
        self.config = config
        self.local_host = local_host
        self.libs_path = f"{config.simple_home}/libs"

        self.package_urls: Dict[str, str] = {
            "java": "https://github.com/adoptium/temurin11-binaries/releases/download"
                    f"/jdk-{config.get_version('java').replace('+', '%2B')}",
            "scala": f"https://downloads.lightbend.com/scala/{config.get_version('scala')}",
            # FIXME use spark url which has older versions
            "spark": f"https://dlcdn.apache.org/spark/spark-{config.get_version('spark')}",
        }

        self.package_names: Dict[str, str] = {
            "java": f"OpenJDK11U-jdk_x64_linux_hotspot_{config.get_version('java').replace('+', '_')}",
            "scala": f"scala-{config.get_version('scala')}",
            "spark": f"spark-{config.get_version('spark')}-bin-hadoop3"
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

    def spark_config_path(self) -> str:
        spark_home = self.package_home_directory("spark")
        return f"{spark_home}/conf/spark-defaults.conf"

    def spark_env_sh_path(self) -> str:
        spark_home = self.package_home_directory("spark")
        return f"{spark_home}/conf/spark-env.sh"
